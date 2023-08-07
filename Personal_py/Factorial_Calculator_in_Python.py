def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive approach

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            result = factorial(num)
            print(f"Factorial of {num} is {result}")
        except ValueError as e:
            print("Invalid input. Please enter a valid integer.")
        except TypeError as e:
            print(str(e))
        except Exception as e:
            print("An error occurred:", str(e))
