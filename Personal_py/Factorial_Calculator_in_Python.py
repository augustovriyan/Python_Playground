def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        factorial_result = 1
        for i in range(1, n + 1):
            factorial_result *= i
        return factorial_result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = factorial(num)
        print("Factorial of {} is {}".format(num, result))
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print("An error occurred:", str(e))
        
