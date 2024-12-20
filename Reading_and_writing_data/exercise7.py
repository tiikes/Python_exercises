fruits = ["apple", "banana", "cherry"]
with open('fruits.txt', 'w') as file:
    for fruit in fruits:
        file.write(fruit + '\n')