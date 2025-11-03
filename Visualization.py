import json
import datetime as dt
import matplotlib.pyplot as plt
import os

from timer import StudyTimer



def graph():
    FILE = "timer_data.json"
    DETAIL = "detail_data.json"

    try:
        data_timer = json.load(open(FILE))
    except Exception:
        data_timer = []

    try:
        data_detail = json.load(open(DETAIL))
    except Exception:
        data_detail = []

    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                learning_records = json.load(f)
        except json.JSONDecodeError:
            print("No data")
            learning_records = []
    else:
        print("No data")
        learning_records = []

    daily_total = {}
    for record in learning_records:
        day = record.get("date")
        try:
            seconds = float(record.get("duration_sec", 0))
        except Exception:
            seconds = 0.0
        if day is None:
            continue
        if day not in daily_total:
            daily_total[day] = 0.0
        daily_total[day] += seconds

    if len(daily_total) == 0:
        print("No record")
        return

    dates_list = []
    for i in daily_total.keys():
        try:
            dates_list.append(dt.date.fromisoformat(i))
        except Exception:
            continue

    day_hour = []
    for i in dates_list:
        hours_today = daily_total[i.strftime("%Y-%m-%d")] / 3600.0
        day_hour.append([i, hours_today])

    def getdate(item):
        return item[0]

    day_hour.sort(key=getdate)
    x = [a[0] for a in day_hour]
    y = [a[1] for a in day_hour]

    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.plot(x, y, marker="o", color="red")
    plt.title("Daily Study Time")
    plt.xlabel("Date")
    plt.ylabel("Hours Studied")
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    plt.bar(x, y)
    plt.title("Daily Study Time")
    plt.xlabel("Date")
    plt.ylabel("Hours Studied")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
    a = input("Type start to begin or type show to see the graph: ")
    if a == "start":
        StudyTimer().run()
        graph()
    else:
        graph()

