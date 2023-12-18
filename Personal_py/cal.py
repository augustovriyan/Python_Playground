# Define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        if y == 0:
            raise ZeroDivisionError
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    try:
        result = x % y
        if y == 0:
            raise ZeroDivisionError
        return result
    except ZeroDivisionError:
        return "Error! Modulus by zero."

# Display calculator menu
def display_menu():
    print("Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")

# User input for operation choice
while True:
    display_menu()
    choice = input("Enter choice (1-6): ")
    
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        result = None

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = exponentiate(num1, num2)
        elif choice == '6':
            result = modulus(num1, num2)

        if isinstance(result, str):
            print(result)
        else:
            operation = {'1': '+', '2': '-', '3': '*', '4': '/', '5': '**', '6': '%'}
            print(f"{num1} {operation[choice]} {num2} = {result}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    else:
        print("Invalid input. Please try again.")
