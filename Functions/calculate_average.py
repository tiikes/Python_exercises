def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [8, 8, 10, 6, 7, 4]
average = calculate_average(numbers)
print(average)