input_string = input("Enter a string: ")
count = {}

for character in input_string:
    if character in count:
        count[character] += 1
    else:
        count[character] = 1

print("Frequency: ", count)