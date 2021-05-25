print("Hello Computer")
Grade = int(input("Please input score: "))

if Grade >= 70 and Grade <= 100:
    print ("You got an A")
elif Grade < 70 and Grade >= 60:
    print("You got a B")
elif Grade <=59 and Grade >= 50:
    print("You got C.")
elif Grade <= 49 and Grade >= 45:
    print ("You got D.")
elif Grade <=44 and Grade >= 40:
    print ("You got E.")
elif Grade <= 39 and Grade >= 0:
    print ("You got an F.")
else:
    print("The number inputted is not in range.")
