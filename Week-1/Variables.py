# Creating variables by storing
a= 10
name = 'Ayesha Malik'
print(f'My name is {name}')

# Data Types
age= int(20)                              #integer it stores whole numbers 
std_name= str("Ayesha Malik")             #string it stores text
height= float(4.9)                        #float it stores decimal numbers
is_student= bool(True)                    #boolean it stores True or False values

# Dictionary it stores key-value pairs
marks = {                                 
    "Math": 88,
    "Python": 92,
    "AI": 85
}

print(f"Her name is {name}")
print(f"Her age is {age}")
print(f"Her height is {height}")
print(f"Is she a student? {is_student}")
print(f"Her marks are {marks}")

# Get the data type of a variable with the type() function.
print(type(name))
print(type(height))
print(type(a))

# Lists it stores multiple values in a single variable
numbers = [28, 30, 27, 29, 31]
print(numbers)

# Methods to manipulate lists
numbers.append(32)  # Adding a new number to the list
numbers.insert(2, 26)  # Inserting a number at index 2
numbers.remove(30)  # Removing a number from the list
print(numbers)
print(len(numbers))  # Getting the length of the list
print(numbers[:3]) # Slicing the list to get the first two elements
numbers.sort()  # Sorting the list in ascending order
print(numbers)

# Favorite Subjects List
subjects = ["Math", "Python", "AI"]
print("I love studying", subjects)


# Take length and width from the user and print the area.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

