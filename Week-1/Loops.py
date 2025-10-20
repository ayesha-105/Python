''' For loops in Python, a for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).
also it use to execute a block of code a fixed number of times.'''

# Iterating through a string
name = "Ayesha Malik"
for x in name:
    print(x)

# Reverse iterating through a string
name = "Ayesha Malik"
reversed_name= ""
for x in name:
    reversed_name= x + reversed_name
print(reversed_name)

# Iterating through a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# Iterating through a tuple
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)

# Iterating through a dictionary
StudentInfo = {
    "name": "Ayesha",
    "age": 20,
    "is_student": True
}
for key in StudentInfo:
    print(f"{key}: {StudentInfo[key]}")  

# Using the range() function

# It will iterate from 0 to 4
for i in range(5):  
    print(i)

# It will iterate from 2 to 5
for j in range(2, 6):
    print(j)

# It will iterate from 0 to 8 with a step of 2
for k in range(0, 10, 2):
    print(k)

# Nested for loops
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")

# using Break statement, it will exit the loop when the condition is met
for num in range(10):
    print(num)
    if num == 5:     
        break  # Exit the loop when num is 5

for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5, ", but this time the break comes before the print
    print(num)

# using Continue statement, it will skip the current iteration when the condition is met
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Take input from user to print multiplication table
tab = int(input("Which number of table do you want: " ))
num = int(input("How many times of table do you want: " ))

for i in range(num):
    print(f"{tab} x {i + 1} = {tab * (i+1)}")


''' While loops in Python, a while loop is used to execute a block of code as 
long as the condition is true.'''

# This will print numbers from 1 to 5
i = 1
while i < 6:
  print(i)
  i += 1

# Using break statement to exit the loop when num is 3  
num= 1
while num < 6:
  print(num)
  if num == 3:
    break
  num += 1

# Using continue statement to skip the number 3
j= 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)

# Using else statement with while loop, the else block will execute when the condition becomes false
count = 9
while count <= 5:
  print(f"Counting: {count}")
  count += 1
else:
  print("Counting finished!")

# while True creates an infinite loop that keeps running until a 'break' statement is executed
while True:
  rollno = input("Enter your 4 digit roll number: ")
  if len(rollno) == 4:
    print("Valid roll number.")
    break
  else:
    print("Invalid roll number. Please try again.")
