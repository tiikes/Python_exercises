password = "monkeymonkey1S"

if len(password) < 8: #checks if password is shorter than 8 characters. If it is, print message.
    print("Password is too short. Must contain at least 8 characters.")


elif not any(char.isdigit() for char in password): #check if password contains a number. If not, print message.
    print("Password must contain a number.")

elif not any(char.isupper() for char in password): #check if password contains a capital letter. If not, print message.
    print("Password must contain a capital letter.")

elif not any(char.islower() for char in password): #check if password contains a small letter. If not, print message.
    print("Password must contain a small letter.")
    
else: #if all above conditions pass, password is strong and the message below is printed to console.
    print("Password is strong.")