def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = factorial(num)
        print("Factorial of {} is {}".format(num, result))
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print("An error occurred:", str(e))
