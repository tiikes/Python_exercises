user_input = -1

while user_input <= 0:
    print("Enter positive integer ")
    user_input = int(input())
    if (user_input < 0):
        print("Not a positive integer.")

print(f"Given integer: {user_input}")