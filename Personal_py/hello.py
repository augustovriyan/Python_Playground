
print("Hello")
name = input("Please enter your name: ")
print("Hello", name + ", How may I assist you today?")

#fUNCTIONS
def print_menu():
    print("Prompt options:")
    print("1. Clock")
    print("2. Weather")
    print("3. Date")
    print("4. Note")
    print("Next 0")

def print_menu2():
    print("Prompt options 2:")
    print("5. Schedule")
    print("6. Browser")
    print("7. Alarm")
    print("8. Stopwatch")
    print("9. Go back to the first prompt")
    print("0. Exit")
    print("END PAGE")

current_menu = "menu1"

while True:
    if current_menu == "menu1":
        print_menu()
        choice = input("Please enter your choice (1-4, 0): ")
        print("You chose:", choice)

        if choice == '1':
            # Perform actions for option 1 (Clock)
            pass
        elif choice == '2':
            # Perform actions for option 2 (Weather)
            pass
        elif choice == '3':
            # Perform actions for option 3 (Date)
            pass
        elif choice == '4':
            # Perform actions for option 4 (Note)
            pass
        elif choice == '0':
            current_menu = "menu2"  # Switch to the second menu
            continue  # Continue to the next iteration

    elif current_menu == "menu2":
        print_menu2()
        choice = input("Please enter your choice (5-9, 0): ")
        print("You chose:", choice)

        if choice == '5':
            # Perform actions for option 5 (Schedule)
            pass
        elif choice == '6':
            # Perform actions for option 6 (Browser)
            pass
        elif choice == '7':
            # Perform actions for option 7 (Alarm)
            pass
        elif choice == '8':
            # Perform actions for option 8 (Stopwatch)
            pass
        elif choice == '9':
            current_menu = "menu1"  # Switch back to the first menu
            continue  # Continue to the next iteration
        elif choice == '0':
            break  # Exit the program

print("EXIT")
