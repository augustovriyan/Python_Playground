import secrets
import string

# Constants
MIN_PASSWORD_LENGTH = 8

def generate_password(length=12, use_punctuation=True):
    characters = string.ascii_letters + string.digits
    if use_punctuation:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            password_length = int(input("Enter the desired password length (minimum {}): ".format(MIN_PASSWORD_LENGTH)))
            if password_length < MIN_PASSWORD_LENGTH:
                print("Password length must be greater than or equal to {}.".format(MIN_PASSWORD_LENGTH))
            else:
                return password_length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    password_length = get_password_length()
    password = generate_password(password_length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
