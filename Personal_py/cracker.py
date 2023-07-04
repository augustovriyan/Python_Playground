import math

def calculate_crack_time(password_length, character_space, attempts_per_second=10**6):
    if password_length == 0:
        return "instantly"
    possibilities = character_space ** password_length
    seconds = possibilities / attempts_per_second
    time = seconds_to_readable_time(seconds)
    return time

def seconds_to_readable_time(seconds):
    intervals = (
        ('years', 31536000),  # 60 seconds * 60 minutes * 24 hours * 365 days
        ('months', 2592000),  # 60 seconds * 60 minutes * 24 hours * 30 days
        ('weeks', 604800),    # 60 seconds * 60 minutes * 24 hours * 7 days
        ('days', 86400),      # 60 seconds * 60 minutes * 24 hours
        ('hours', 3600),      # 60 seconds * 60 minutes
        ('minutes', 60),
        ('seconds', 1)
    )

    result = []

    for name, count in intervals:
        value = math.floor(seconds / count)
        if value:
            seconds -= value * count
            result.append(f"{value} {name}")

    return ', '.join(result)

# Main program
if __name__ == "__main__":
    while True:
        password = input("Enter the password (6-12 characters) (enter '0' to exit): ")

        if password == '0':
            print("Exiting the program...")
            break

        password_length = len(password)

        if password_length < 6 or password_length > 12:
            print("Password length should be between 6 and 12 characters.")
            continue

        character_space = len(set(password))

        if character_space == 0:
            print("Password should contain at least one character.")
            continue

        crack_time = calculate_crack_time(password_length, character_space)
        print("Estimated crack time:", crack_time)
