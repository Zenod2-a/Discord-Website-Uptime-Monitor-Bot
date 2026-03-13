from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import os

app = FastAPI()

LOG_FILE = "monitor_log.csv"


@app.get("/", response_class=HTMLResponse)
def dashboard():

    if not os.path.exists(LOG_FILE):
        return "<h2>No monitoring data yet</h2>"

    try:
        data = pd.read_csv(LOG_FILE)
    except:
        return "<h2>Log file error</h2>"

    if data.empty:
        return "<h2>No monitoring events yet</h2>"

    total_events = len(data)
    down_events = len(data[data["status"] == "DOWN"])
    up_events = len(data[data["status"] == "UP"])

    recent = data.tail(10)

    html = f"""
    <html>
    <head>
    <title>Website Monitoring Dashboard</title>
    <style>
    body {{ font-family: Arial; background:#111; color:white; padding:40px }}
    table {{ border-collapse: collapse; width:100% }}
    th, td {{ border:1px solid #444; padding:8px }}
    th {{ background:#333 }}
    .down {{ color:red }}
    .up {{ color:lime }}
    </style>
    </head>

    <body>

    <h1>Website Monitoring Dashboard</h1>

    <h3>Total Events: {total_events}</h3>
    <h3 style="color:red">Down Events: {down_events}</h3>
    <h3 style="color:lime">Recovery Events: {up_events}</h3>

    <h2>Recent Events</h2>

    <table>
    <tr>
    <th>Time</th>
    <th>URL</th>
    <th>Status</th>
    <th>Latency</th>
    </tr>
    """

    for _, row in recent.iterrows():

        status_class = "down" if row["status"] == "DOWN" else "up"

        html += f"""
        <tr>
        <td>{row['time']}</td>
        <td>{row['url']}</td>
        <td class="{status_class}">{row['status']}</td>
        <td>{row['latency']}</td>
        </tr>
        """

    html += "</table></body></html>"

    return html