import math

def calculate_crack_time(password_length, character_space, attempts_per_second=10**6):
    if password_length == 0:
        return "instantly"
    possibilities = character_space ** password_length
    seconds = possibilities / attempts_per_second
    return seconds_to_readable_time(seconds)

def seconds_to_readable_time(seconds):
    intervals = [
        ('year', 31536000),  # 60 seconds * 60 minutes * 24 hours * 365 days
        ('month', 2592000),  # 60 seconds * 60 minutes * 24 hours * 30 days
        ('week', 604800),    # 60 seconds * 60 minutes * 24 hours * 7 days
        ('day', 86400),      # 60 seconds * 60 minutes * 24 hours
        ('hour', 3600),      # 60 seconds * 60 minutes
        ('minute', 60),
        ('second', 1)
    ]

    time_parts = []

    for name, count in intervals:
        value = math.floor(seconds / count)
        if value:
            time_parts.append(f"{value} {name}{'s' if value > 1 else ''}")
            seconds -= value * count

    return ', '.join(time_parts)

def is_strong_password(password):
    length = len(password)
    character_space = len(set(password))

    if length < 6 or length > 12:
        return False, "Password length should be between 6 and 12 characters."

    if character_space < 4:
        return False, "Password should contain at least four different characters."

    requirements = {
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special': any(not char.isalnum() for char in password),
    }

    if all(requirements.values()):
        return True, "Strong password"
    else:
        return False, "Password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."

if __name__ == "__main__":
    while True:
        password = input("Enter the password (6-12 characters) (enter '0' to exit): ")

        if password == '0':
            print("Exiting the program...")
            break

        is_strong, message = is_strong_password(password)

        if is_strong:
            password_length = len(password)
            character_space = len(set(password))
            crack_time = calculate_crack_time(password_length, character_space)
            print("Estimated crack time:", crack_time)
        else:
            print(message)
