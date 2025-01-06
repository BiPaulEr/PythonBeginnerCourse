def analyze_data(data):
    if not data:
        return "No data provided"
    if len(data) < 5:
        return "Insufficient data"
    if len(data) == 5:
        return "Minimum data received"

    total = sum(data)
    if total > 100:
        return "Data sum exceeds maximum threshold"
    if total < 50:
        return "Data sum below minimum threshold"
    if total == 75:
        return "Data sum is exactly 75"
    if total % 2 == 0:
        return "Data sum is even"
    if total % 2 != 0:
        return "Data sum is odd"

    max_value = max(data)
    if max_value > 50:
        return "Maximum value in data exceeds 50"
    if max_value < 10:
        return "Maximum value in data is below 10"
    if max_value == 25:
        return "Maximum value is exactly 25"

    min_value = min(data)
    if min_value < 5:
        return "Minimum value in data is below 5"
    if min_value > 20:
        return "Minimum value in data exceeds 20"
    return "Data is within acceptable range"