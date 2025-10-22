import time, json, datetime

TODAY = datetime.date.today()
FILE = "timer_data.json"
data = json.load(open(FILE))

input("press enter to start")
start = time.time()
input("press again to end")
end = time.time()
duration = end - start
# print(f"{duration:.1f} seconds.")

data.append(
    {"date": str(TODAY),
    "duration_sec": round(duration, 1)}
    )

with open(FILE, "w") as f:
    json.dump(data, f)


# print(data)