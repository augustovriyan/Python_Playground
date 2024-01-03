import secrets
import string

# Constants
MIN_LENGTH = 8
DEFAULT_LENGTH = 12

def generate_password(length=DEFAULT_LENGTH, include_punctuation=True):
    """Generate a random password with the given length and option to include punctuation.

    Args:
        length (int): Length of the password (default is 12).
        include_punctuation (bool): Include punctuation characters (default is True).

    Returns:
        str: A randomly generated password.
    """
    characters = string.ascii_letters + string.digits
    if include_punctuation:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))

def get_valid_length():
    """Prompt user to input a valid password length."""
    while True:
        try:
            user_input = input(f"Enter the desired password length (minimum {MIN_LENGTH}): ")
            if not user_input:
                return DEFAULT_LENGTH
            length = int(user_input)
            if length < MIN_LENGTH:
                print(f"Password length must be at least {MIN_LENGTH}.")
            else:
                return length
        except (ValueError, KeyboardInterrupt):
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to generate a password."""
    print("Password Generator")
    length = get_valid_length()
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
