def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

while True:
    year = input("Enter a year (0 to exit): ")

    if year == "0":
        print("Exiting the program...")
        break

    try:
        year = int(year)
    except ValueError:
        print("Invalid input. Please input numeric value only for the year leap to work.")
        continue

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
