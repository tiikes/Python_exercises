user_input = input("Enter a sentence: ")

tuple_words = tuple(user_input.split())
reverse = tuple(reversed(tuple_words))

print("Words: ", reverse)