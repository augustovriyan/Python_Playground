# Welcome the user and get their name
print("Hello!")
name = input("Please enter your name: ")
print(f"Hello, {name}! How may I assist you today?\n")

# Function to display the main menu
def print_menu():
    print("Main Menu Options:")
    print("1. Clock")
    print("2. Weather")
    print("3. Date")
    print("4. Note")
    print("0. Next Menu")

# Function to display the secondary menu
def print_menu2():
    print("\nSecondary Menu Options:")
    print("5. Schedule")
    print("6. Browser")
    print("7. Alarm")
    print("8. Stopwatch")
    print("9. Return to Main Menu")
    print("0. Exit")

# Initialize the current menu
current_menu = "menu1"

while True:
    if current_menu == "menu1":
        print_menu()
        choice = input("\nPlease enter your choice (1-4, 0): ")

        if choice == '1':
            print("You selected: Clock")
            # Implement clock functionality here
        elif choice == '2':
            print("You selected: Weather")
            # Implement weather functionality here
        elif choice == '3':
            print("You selected: Date")
            # Implement date functionality here
        elif choice == '4':
            print("You selected: Note")
            # Implement note functionality here
        elif choice == '0':
            current_menu = "menu2"
            continue

    elif current_menu == "menu2":
        print_menu2()
        choice = input("\nPlease enter your choice (5-9, 0): ")

        if choice == '5':
            print("You selected: Schedule")
            # Implement schedule functionality here
        elif choice == '6':
            print("You selected: Browser")
            # Implement browser functionality here
        elif choice == '7':
            print("You selected: Alarm")
            # Implement alarm functionality here
        elif choice == '8':
            print("You selected: Stopwatch")
            # Implement stopwatch functionality here
        elif choice == '9':
            current_menu = "menu1"
            continue
        elif choice == '0':
            print("Exiting the program.")
            break

print("\nProgram has exited.")
