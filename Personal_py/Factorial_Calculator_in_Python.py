def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = factorial(num)
    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial of {} is {}".format(num, result))
