import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
"credentials.json", scope
)

client = gspread.authorize(creds)

sheet = client.open("URL Monitor").sheet1

print(sheet.col_values(1))