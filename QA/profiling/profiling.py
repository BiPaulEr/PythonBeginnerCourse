from memory_profiler import profile

@profile
def sum_of_squares(n):
    return sum([i**2 for i in range(1, n + 1)])

def main():
    for i in range (1, 20):
        result = sum_of_squares(10000)
        print("Sum of squares:", result)

if __name__ == "__main__":
    main()