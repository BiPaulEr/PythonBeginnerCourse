import pdb
import sys

def divide_numbers(a, b):
    return a / b

def main():
    try:
        num1 = 10
        num2 = 0 
        result = divide_numbers(num1, num2)
        print(f"Résultat : {result}")
    except Exception:
        pdb.post_mortem(sys.exc_info()[2])

if __name__ == "__main__":
    main()
