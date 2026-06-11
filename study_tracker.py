subjects = {}

while True:
    print("\n=== STUDY TRACKER ===")
    print("1. Add study session")
    print("2. View total hours")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Subject name: ")
        hours = float(input("Hours studied: "))

        if subject in subjects:
            subjects[subject] += hours
        else:
            subjects[subject] = hours

        print(f"{hours} hours added to {subject}.")

    elif choice == "2":
        print("\nStudy Summary:")

        total = 0

        for subject, hours in subjects.items():
            print(f"{subject}: {hours} hours")
            total += hours

        print(f"\nTotal study time: {total} hours")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")