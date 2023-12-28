# Define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error! Division by zero.")
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        raise ValueError("Error! Modulus by zero.")
    return x % y

# Display calculator menu
def display_menu():
    print("\nCalculator Menu")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")

# Main calculator loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        # Perform the selected operation
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': exponentiate,
            '6': modulus
        }

        try:
            result = operations[choice](num1, num2)
            print(f"\nResult: {num1} {'+'.join(['', '-', '*', '/', '**', '%'][int(choice) - 1])} {num2} = {result}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask if the user wants to continue
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    else:
        print("Invalid input! Please select a valid option.")
