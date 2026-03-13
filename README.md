# Discord Website Uptime Monitor Bot

A high-performance **Python Discord bot** that monitors thousands of websites and sends real-time alerts when a site goes **DOWN or comes back ONLINE**.

This bot reads URLs from a CSV dataset and checks them asynchronously using Python's async libraries, making it capable of monitoring **thousands of websites efficiently**.

---

## 🚀 Features

* Monitor **thousands of websites automatically**
* **Asynchronous URL checking** using aiohttp
* **Batch processing** for efficient resource usage
* **Discord alerts** when website status changes
* Detects:

  * Website **DOWN**
  * Website **BACK ONLINE**
* Configurable **monitoring interval**
* Lightweight and easy to deploy

---

## 🛠️ Technologies Used

* Python 3.9+
* Discord.py
* aiohttp
* asyncio
* pandas

---

## 📂 Project Structure

```
website-uptime-monitor/
│
├── bot.py
├── urls_10000.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/website-uptime-monitor.git
cd website-uptime-monitor
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```
discord.py
aiohttp
pandas
```

---

## 🤖 Create a Discord Bot

1. Go to the Discord Developer Portal
2. Create a **New Application**
3. Navigate to **Bot**
4. Click **Add Bot**
5. Copy the **Bot Token**

Replace the token in the code:

```
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

---

## 📡 Setup Discord Channel

Find your **Channel ID** and replace:

```
CHANNEL_ID = YOUR_CHANNEL_ID
```

Enable Developer Mode in Discord to copy channel IDs.

---

## 📊 CSV Dataset Format

Your CSV file should look like this:

```
URL
https://google.com
https://github.com
https://example.com
```

You can monitor **thousands of URLs** by adding them to this file.

---

## ▶️ Run the Bot

```
python bot.py
```

If everything works correctly, you will see:

```
Bot started successfully
```

---

## 🔔 Alert Examples

When a site goes down:

```
🚨 Site DOWN: https://example.com
```

When it comes back online:

```
✅ Site BACK ONLINE: https://example.com
```

---

## ⚡ Performance

Default configuration:

* **Batch Size:** 100 websites
* **Monitoring Interval:** 3 minutes
* **Async HTTP requests** for high performance

This allows monitoring **10,000+ websites efficiently**.

---

## 🔒 Security Notice

⚠️ **Never expose your Discord bot token publicly.**

If your token is leaked:

1. Go to the Discord Developer Portal
2. Reset the bot token
3. Update it in your code

---

## 🧠 Possible Improvements

Future enhancements could include:

* Website **response time monitoring**
* **Web dashboard** for monitoring statistics
* **Database storage** for uptime history
* **Email or SMS alerts**
* **Docker deployment**
* Real-time monitoring UI

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you find this project useful, consider **starring the repository** on GitHub.

---

## 👨‍💻 Author
       Gaurav Panday
