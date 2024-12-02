def find_maximum(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number

    return(max_number)

numbers = [4, 5, 9, 2, 11, 25, 3]
max_number = find_maximum(numbers)
print(max_number)