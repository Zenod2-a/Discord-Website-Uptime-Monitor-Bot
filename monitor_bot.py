import discord
import aiohttp
import asyncio
import time
import csv
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ========================
# CONFIGURATION
# ========================

TOKEN = "Add you Discord Bot Token "
CHANNEL_ID = Add you Discord Channel ID

CHECK_INTERVAL = 180
BATCH_SIZE = 100
RETRY_COUNT = 3
MAX_CONCURRENT_REQUESTS = 50

# ========================
# GOOGLE SHEETS SETUP
# ========================

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

gs_client = gspread.authorize(creds)

sheet = gs_client.open("URL Monitor").sheet1

urls = sheet.col_values(1)[1:]

# ========================
# DISCORD CLIENT
# ========================

status_cache = {}

intents = discord.Intents.default()
client = discord.Client(intents=intents)

semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

# ========================
# LOGGING
# ========================

def log_status(url, status):

    with open("monitor_log.csv", "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([datetime.now(), url, status])


# ========================
# URL CHECKER
# ========================

async def check_url(session, url):

    async with semaphore:

        try:

            start = time.time()

            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:

                latency = round((time.time() - start) * 1000, 2)

                return response.status == 200, latency

        except:

            return False, None


async def check_with_retry(session, url):

    for _ in range(RETRY_COUNT):

        status, latency = await check_url(session, url)

        if status:
            return status, latency

    return False, None


# ========================
# MONITORING ENGINE
# ========================

async def monitor():

    await client.wait_until_ready()

    channel = await client.fetch_channel(1481703144290258964)

    async with aiohttp.ClientSession() as session:

        while True:

            for i in range(0, len(urls), BATCH_SIZE):

                batch = urls[i:i + BATCH_SIZE]

                tasks = [check_with_retry(session, url) for url in batch]

                results = await asyncio.gather(*tasks)

                for j, url in enumerate(batch):

                    status, latency = results[j]

                    state = "Active" if status else "Inactive"

                    if url not in status_cache:
                        status_cache[url] = state
                        continue

                    if status_cache[url] != state:

                        status_cache[url] = state

                        if state == "Inactive":

                            embed = discord.Embed(
                                title="🚨 Website Down",
                                description=url,
                                color=discord.Color.red()
                            )

                            await channel.send(embed=embed)

                            log_status(url, "DOWN")

                        else:

                            embed = discord.Embed(
                                title="✅ Website Back Online",
                                description=f"{url}\nLatency: {latency} ms",
                                color=discord.Color.green()
                            )

                            await channel.send(embed=embed)

                            log_status(url, "UP")

                print(f"Checked batch {i // BATCH_SIZE + 1}")

            print("Waiting before next check...")

            await asyncio.sleep(CHECK_INTERVAL)


# ========================
# DISCORD EVENTS
# ========================

@client.event
async def on_ready():

    print("Bot started successfully")

    client.loop.create_task(monitor())


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == "!ping":

        await message.channel.send("Bot is running and monitoring URLs.")


# ========================
# START BOT
# ========================

client.run(TOKEN)
