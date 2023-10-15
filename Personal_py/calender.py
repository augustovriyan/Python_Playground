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

def print_calendar_header(year, month):
    print(f"{calendar.month_name[month]} {year}")
    print(" ".join(WEEKDAYS))

def print_calendar_body(cal):
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

    cal = calendar.monthcalendar(year, month)
    
    print_calendar_header(year, month)
    print_calendar_body(cal)

if __name__ == "__main__":
    main()
