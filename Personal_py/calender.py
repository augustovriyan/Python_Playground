import calendar

WEEKDAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

def get_validated_input(prompt, validator):
    """Validate user input using the provided validator function."""
    while True:
        user_input = input(prompt)
        try:
            validated_input = validator(user_input)
            return validated_input
        except ValueError:
            print("Invalid input. Please try again.")

def print_calendar(year, month):
    """Print the calendar for the specified year and month."""
    # Fetch the calendar matrix for the given year and month
    cal_matrix = calendar.monthcalendar(year, month)

    # Display the calendar header
    print(f"\n{calendar.month_name[month]} {year}")
    print(" ".join(WEEKDAYS))

    # Display the calendar body
    for week in cal_matrix:
        for day in week:
            if day == 0:
                print("   ", end=" ")  # Display empty space for days not in the current month
            else:
                print(f"{day:3d}", end=" ")  # Format and display the day
        print()  # Move to the next line for the next week

def main():
    """Main function to get user input and display the calendar."""
    # Get and validate the year from the user
    year = get_validated_input("Enter the year: ", lambda x: int(x))

    # Get and validate the month from the user (1-12)
    while True:
        month = get_validated_input("Enter the month: ", lambda x: int(x))
        if 1 <= month <= 12:
            break
        else:
            print("Invalid month. Please enter a valid month (1-12).")

    # Display the calendar for the specified year and month
    print_calendar(year, month)

if __name__ == "__main__":
    main()
