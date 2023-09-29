def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    return x % y

print("Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Modulus")

while True:
    choice = input("Enter choice (1-6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
        elif choice == '6':
            result = modulus(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} % {num2} = {result}")
        break
    else:
        print("Invalid input. Please try again.")
