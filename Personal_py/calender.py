import calendar

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Create the calendar for the specified year and month
cal = calendar.monthcalendar(year, month)

# Print the calendar
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print()
