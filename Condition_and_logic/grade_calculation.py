score = 75 #set a grade
if (score >= 90 and score <= 100): #if score is 90-100, print grade A
    print("A")
elif (score >= 80 and score <= 89): #if score is 80-89, print grade B
    print("B")
elif (score >= 70 and score <= 79): #if score is 70-79, print grade C
    print("C")
elif (score >= 60 and score <= 69): #if score is 60-69, print grade D
    print("D")
elif (score >= 0 and score <= 59): #if score is 0-59, print grade F
    print("F")
else: #if score isn't in the range of 0-100, print "Invalid score"
    print("Invalid score.")