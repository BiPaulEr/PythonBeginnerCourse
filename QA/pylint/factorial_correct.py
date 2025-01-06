"""
[factorial]

Description :
    Module de math.
"""

def factorial(num):
    """
    Calcule la factorielle d'un nombre entier donné.
    """
    if num < 0:
        return "No factorial for negative numbers"
    if num == 0:
        return 1
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

result = factorial(5)
print("The factorial of 5 is", result)
