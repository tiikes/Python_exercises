file = open('data.txt', 'r')
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)