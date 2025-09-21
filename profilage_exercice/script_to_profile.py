import random
from memory_profiler import profile

# Générer des données simulées
def generate_data(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Fonction pour calculer la moyenne et le max
@profile
def stats_list(data):
    # Utilisation d'une liste comprehension (plus gourmand en mémoire)
    squared = [x**2 for x in data]
    return {
        "sum": sum(squared),
        "max": max(squared),
        "min": min(squared),
        "average": sum(squared) / len(squared)
    }

@profile
def stats_generator(data):
    # Utilisation d'un générateur (moins gourmand)
    squared_gen = (x**2 for x in data)
    total = 0
    count = 0
    max_val = float("-inf")
    min_val = float("inf")

    for x in squared_gen:
        total += x
        count += 1
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    return {
        "sum": total,
        "max": max_val,
        "min": min_val,
        "average": total / count
    }

def main():
    data = generate_data(10**6)  # 1 000 000 valeurs

    print("Stats avec list comprehension :")
    result_list = stats_list(data)
    print(result_list)

    print("Stats avec generator :")
    result_gen = stats_generator(data)
    print(result_gen)

if __name__ == "__main__":
    main()
