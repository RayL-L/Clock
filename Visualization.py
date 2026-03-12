import json
import datetime as dt
import matplotlib.pyplot as plt
import os

from timer import StudyTimer


def get_streak(records):
    dates = []

    for record in records:
        day = record.get("date")
        if day is not None:
            dates.append(dt.date.fromisoformat(day))

    dates = sorted(list(set(dates)))

    if len(dates) == 0:
        return 0, 0

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 1

    today = dt.date.today()
    streak_now = 0

    if len(dates) > 0:
        if dates[-1] == today:
            streak_now = 1
            for i in range(len(dates) - 1, 0, -1):
                if (dates[i] - dates[i - 1]).days == 1:
                    streak_now += 1
                else:
                    break

    return streak_now, longest_streak


def draw_line_graph(x, y, avg):
    plt.subplot(2, 2, 1)

    plt.plot(x, y, marker="o", color="red", label="Daily Hours")
    plt.plot(x, avg, label="Rolling Avg")

    plt.title("Daily Study Time - Line")
    plt.xlabel("Date")
    plt.ylabel("Hours")
    plt.xticks(rotation=45)
    plt.legend()


def draw_bar_graph(x, y):
    plt.subplot(2, 2, 2)

    plt.bar(x, y)

    plt.title("Daily Study Time - Bar")
    plt.xlabel("Date")
    plt.ylabel("Hours")
    plt.xticks(rotation=45)


def draw_subject_percentage_graph(records):
    plt.subplot(2, 2, 3)

    subject_total = {}

    for record in records:
        subject = record.get("subject", "General")
        seconds = float(record.get("duration_sec", 0))

        if subject not in subject_total:
            subject_total[subject] = 0.0

        subject_total[subject] += seconds

    labels = list(subject_total.keys())
    sizes = list(subject_total.values())

    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)

    plt.title("Subject Percentage")


def graph():
    FILE = "timer_data.json"

    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            learning_records = json.load(f)
    else:
        print("No data")
        return

    daily_total = {}

    for record in learning_records:
        day = record.get("date")
        seconds = float(record.get("duration_sec", 0))

        if day not in daily_total:
            daily_total[day] = 0.0

        daily_total[day] += seconds

    dates_list = []

    for i in daily_total.keys():
        dates_list.append(dt.date.fromisoformat(i))

    day_hour = []

    for i in dates_list:
        hours_today = daily_total[i.strftime("%Y-%m-%d")] / 3600.0
        day_hour.append([i, hours_today])

    day_hour.sort(key=lambda item: item[0])

    x = [a[0] for a in day_hour]
    y = [a[1] for a in day_hour]

    avg = []

    for i in range(len(y)):
        avg.append(sum(y[:i+1]) / (i+1))

    current_streak, longest_streak = get_streak(learning_records)

    print("Current streak:", current_streak, "day(s)")
    print("Longest streak:", longest_streak, "day(s)")

    plt.figure(figsize=(15, 10))

    draw_line_graph(x, y, avg)
    draw_bar_graph(x, y)
    draw_subject_percentage_graph(learning_records)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    a = input("Type start to begin or type show to see the graph: ")

    if a == "start":
        StudyTimer().run()
        graph()
    else:
        graph()
