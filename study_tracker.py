import time
import json
from datetime import datetime

DATA_FILE = "study_data.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def start_study(subject):

    print(f"\n📚 Studying: {subject}")
    input("Press ENTER to start timer")

    start = time.time()

    input("Press ENTER to stop study session")

    end = time.time()

    duration = round((end - start) / 60, 2)

    print(f"⏱ Study Time: {duration} minutes")

    today = str(datetime.today().date())

    data = load_data()

    if today not in data:
        data[today] = {}

    if subject not in data[today]:
        data[today][subject] = 0

    data[today][subject] += duration

    save_data(data)


def show_report():

    data = load_data()

    print("\n📊 Study Report\n")

    for date in data:

        print(f"\nDate: {date}")

        for subject in data[date]:

            print(f"{subject} → {data[date][subject]} minutes")


def productivity_score():

    data = load_data()

    total = 0

    for date in data:
        for subject in data[date]:
            total += data[date][subject]

    score = total / 60

    print(f"\n🔥 Total Study Hours: {round(score,2)}")

    if score > 20:
        print("🚀 Productivity Level: Excellent")
    elif score > 10:
        print("👍 Productivity Level: Good")
    else:
        print("⚠ Productivity Level: Low")


while True:

    print("\n==== AI Study Tracker ====")
    print("1 Start Study Session")
    print("2 Show Report")
    print("3 Productivity Score")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        start_study(subject)

    elif choice == "2":
        show_report()

    elif choice == "3":
        productivity_score()

    elif choice == "4":
        break