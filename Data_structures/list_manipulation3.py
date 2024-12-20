numbers = [1,2,3,4,5]
remove_duplicates = list(set(numbers))
second_largest = max(num for num in remove_duplicates if num != max(remove_duplicates))

print("Second largest number in list:", second_largest)