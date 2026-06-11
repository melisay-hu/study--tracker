import json
from datetime import datetime

DATA_FILE = "study_data.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_study_session(data):
    subject = input("Subject name: ")
    hours = float(input("Hours studied: "))
    date = datetime.now().strftime("%Y-%m-%d")

    session = {
        "subject": subject,
        "hours": hours,
        "date": date
    }

    data.append(session)
    save_data(data)

    print(f"{hours} hours added for {subject}.")


def view_summary(data):
    summary = {}

    for session in data:
        subject = session["subject"]
        hours = session["hours"]

        if subject in summary:
            summary[subject] += hours
        else:
            summary[subject] = hours

    print("\nStudy Summary:")

    total = 0

    for subject, hours in summary.items():
        print(f"{subject}: {hours} hours")
        total += hours

    print(f"\nTotal study time: {total} hours")


def suggest_subject(data):
    if not data:
        print("No study data yet. Add a study session first.")
        return

    summary = {}

    for session in data:
        subject = session["subject"]
        hours = session["hours"]

        if subject in summary:
            summary[subject] += hours
        else:
            summary[subject] = hours

    least_studied_subject = min(summary, key=summary.get)

    print("\nAI Study Suggestion:")
    print(f"You should focus on: {least_studied_subject}")
    print("Reason: This is your least studied subject so far.")


def view_progress_chart(data):
    summary = {}

    for session in data:
        subject = session["subject"]
        hours = session["hours"]

        if subject in summary:
            summary[subject] += hours
        else:
            summary[subject] = hours

    print("\nStudy Progress Chart:")

    for subject, hours in summary.items():
        bar = "█" * int(hours)
        print(f"{subject}: {bar} {hours}h")


def main():
    data = load_data()

    while True:
        print("\n=== AI STUDY ASSISTANT ===")
        print("1. Add study session")
        print("2. View study summary")
        print("3. Get AI study suggestion")
        print("4. View progress chart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_study_session(data)
        elif choice == "2":
            view_summary(data)
        elif choice == "3":
            suggest_subject(data)
        elif choice == "4":
            view_progress_chart(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


main()