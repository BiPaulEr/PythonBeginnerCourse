def factorial(num):
    if num < 0:
        return "No factorial for negative numbers"
    elif num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact

result = factorial(5)
print("The factorial of 5 is", result)