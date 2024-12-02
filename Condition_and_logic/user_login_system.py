username = input("Enter username: ") #ask for username
password = input("Enter password: ") #ask for password

#if both username and password match the values below, print login successful
if username == "Monkey" and password == "monkey123": 
    print("Login successful")

#if username and/or password don't match, print error message.
else:
    print("Invalid username or password")