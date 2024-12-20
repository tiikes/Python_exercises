try:
    file = open('example.txt', 'r')
    print("File opened successfully")
    file.close()
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
