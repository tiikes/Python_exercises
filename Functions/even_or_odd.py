def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = 11
if is_even(number):
    print("Number is even")
else:
    print("Number is odd")