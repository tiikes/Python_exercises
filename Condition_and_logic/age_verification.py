userAge = input("How old are you?") #ask user to enter their age

age = int(userAge) #convert input string to integer

#if age is under 13, print "child"
if (age < 13): 
    print("You're a child.")

#if age is under 18, print "teenager"
elif (age < 18): 
    print("You're a teenager.")

#if age is 18 or more, print "adult"
else: 
    print("You're an adult.")


