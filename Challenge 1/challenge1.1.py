def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input a number for which you want to calculate the factorial
num = int(input("Enter a non-negative integer: "))

result = factorial(num)

if isinstance(result, int):
    print(f"The factorial of {num} is {result}")
else:
    print(result)
