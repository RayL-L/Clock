import json
import datetime as dt
import matplotlib.pyplot as plt
import os


TODAY = dt.date.today()
FILE = "timer_data.json"
DETAIL = "detail_data.json"
data_timer = json.load(open(FILE))
data_detail = json.load(open(DETAIL))


if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
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
    seconds = float(record.get("duration_sec", 0))
    if day is None:
        continue
    if day not in daily_total:
        daily_total[day] = 0
    daily_total[day] += seconds
if len(daily_total) == 0:
    print("No record")
    quit()


sorted = []
for i in daily_total.keys():
    sorted.append(dt.date.fromisoformat(i))
day_hour = []
for i in sorted:
    hours_today = daily_total[i.strftime("%Y-%m-%d")] / 3600
    day_hour.append([i, hours_today])


def getdate(item):
    return item[0]
day_hour.sort(key=getdate)
x = []
for a in day_hour:
    day = a[0]
    x.append(day)
y = []
for a in day_hour:
    hours = a[1]
    y.append(hours)

plt.figure(figsize=(9, 4))
plt.plot(x, y, marker="o", color="red")
plt.title("Daily Study Time")
plt.xlabel("Date")
plt.ylabel("Hours Studied")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
