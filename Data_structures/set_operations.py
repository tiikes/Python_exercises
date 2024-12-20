input_list1 = input("Enter first list: ")

list1 = [int(num.strip()) for num in input_list1.split(",")]

input_list2 = input("Enter second list: ")

list2 = [int(num.strip()) for num in input_list2.split(",")]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)

print("Intersection: ", intersection)