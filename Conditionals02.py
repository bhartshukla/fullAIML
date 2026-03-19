# If elif , else  (Conditional Statements)

# age = int (input("Enter your Age : "))

# if age>=18:
#     print("You Can Vote")
#     print("You Can Drive")

# else:
#     print("You cant vote")  
# 




color = input("Enter Color : ")

if color == "red":
    print("Stop Now")
elif color == "yellow":
    print("Slow Move")
elif color == "green":
    print("You Can Go")    
else:
    print("Invalid color")    



age = int(input("Enter your number"))

if age >= 18:
    print("You are Adult")
elif age<18 and age>5:    
    print("you are teen")
else:
    print("you are under age or above age")