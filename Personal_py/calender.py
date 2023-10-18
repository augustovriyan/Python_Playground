import calendar

WEEKDAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

def get_validated_input(prompt, validator):
    while True:
        user_input = input(prompt)
        try:
            validated_input = validator(user_input)
            return validated_input
        except ValueError:
            print("Invalid input. Please try again.")

def print_calendar(year, month):
    # Get the calendar matrix for the specified year and month
    cal = calendar.monthcalendar(year, month)

    # Print the calendar header
    print(f"{calendar.month_name[month]} {year}")
    print(" ".join(WEEKDAYS))

    # Print the calendar body
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:3d}", end=" ")
        print()

def main():
    year = get_validated_input("Enter the year: ", lambda x: int(x))
    while True:
        month = get_validated_input("Enter the month: ", lambda x: int(x))
        if 1 <= month <= 12:
            break
        else:
            print("Invalid month. Please enter a valid month (1-12).")

    # Call the print_calendar function to display the calendar
    print_calendar(year, month)

if __name__ == "__main__":
    main()
