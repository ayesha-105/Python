# Conditional Statements in Python if, elif, and else

x= 20
if x > 30:                                   #if conditon is true then only the block will be executed
    print("x is greater than 30")
elif x == 20:                                 #elif is used to check multiple conditions
    print("x is 20")
elif x < 10:                             
    print("x is less than 10")                
else:                                         #else block will be executed if all the above conditions are false
    print("x is between 10 and 30 but not 20")

# Check Positive/Negative/Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Grade checker
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("F")


