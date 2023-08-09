import secrets
import string

def generate_password(length=12, use_punctuation=True):
    characters = string.ascii_letters + string.digits
    if use_punctuation:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length < 1:
                print("Password length must be greater than or equal to 1.")
            else:
                return password_length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    password_length = get_password_length()
    password = generate_password(password_length)
    print("Generated password:", password)
