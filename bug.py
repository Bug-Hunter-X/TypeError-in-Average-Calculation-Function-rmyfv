def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (potential error)
data = [10, 20, 30, 'a']
average = calculate_average(data)
print(f"Average: {average}")