user_input = input("Enter numbers.").split()
numbers = [int(num) for num in user_input]

Sum = sum(numbers)

print("Sum of given numbers: ", Sum)