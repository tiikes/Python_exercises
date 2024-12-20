try:
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)

except FileNotFoundError:
    print("The file does not exist")
