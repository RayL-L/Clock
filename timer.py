import time, json, datetime

class StudyTimer:
    def __init__(self, file_path: str = "timer_data.json", detail_path: str = "detail_data.json") -> None:
        self.FILE = file_path
        self.DETAIL = detail_path



    def run(self) -> None:
        TODAY = datetime.date.today()
        FILE = self.FILE
        DETAIL = self.DETAIL

        data_timer = json.load(open(FILE))
        data_detail = json.load(open(DETAIL))

        ifEnd = False
        ifPause = False

        focusTime = []

        input("press return to start: ")
        start = time.time()

        while ifEnd == False:
            a = input("pause to pause, resume to resume: ")
            if a == "pause":
                end = time.time()
                duration = round((end - start), 1)
                focusTime.append(duration)
                ifPause = True
            elif a == "resume" and ifPause == True:
                start = time.time()
                ifPause = False
            elif a == "":
                if ifPause:
                    ifEnd = True
                    break
                else:
                    end = time.time()
                    duration = round((end - start), 1)
                    focusTime.append(duration)
                    ifEnd = True
                    break

        # print(f"{duration:.1f} seconds.")

        data_timer.append(
            {"date": str(TODAY),
             "duration_sec": round(sum(focusTime), 1)}
        )

        data_detail.append(
            {"date": str(TODAY),
             "duration_details": focusTime}
        )

        with open(FILE, "w") as f:
            json.dump(data_timer, f)

        with open(DETAIL, "w") as f:
            json.dump(data_detail, f)
