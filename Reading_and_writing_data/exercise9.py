try:
    with open('source.txt', 'r') as source_file:
        with open('destination.txt', 'w') as destination_file:
            content = source_file.read()
            destination_file.write(content)
except FileNotFoundError:
    print("Source file does not exist")
