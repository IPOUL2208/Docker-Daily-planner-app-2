import json
import requests
from datetime import datetime

def load_tasks():
    with open("tasks.json") as f:
        return json.load(f)

def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random")
        return res.json().get("content")
    except:
        return "Keep going, you're doing great!"

def print_report():
    print("🗓️ Daily Planner -", datetime.now().strftime("%Y-%m-%d"))
    print("Tasks:")
    for task in load_tasks():
        print(f" - {task}")
    print("\nQuote of the day:")
    print(get_quote())

if __name__ == "__main__":
    print_report()
