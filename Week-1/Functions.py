# Most Common Built-in Functions

# string functions
text = "Ayesha Malik"
print(len(text))                          # Length of string
print(text.upper())                       # Convert to uppercase
print(text.lower())                       # Convert to lowercase
print(text.title())                       # Capitalize first letter of each word
print(text.replace("Ayesha", "Farah"))    # Replace text

# Numeric math functions
num = -7.8
print(abs(num))                    # Absolute value
print(round(3.456, 2))             # Round to 2 decimals
print(max(4, 8, 2, 9))             # Largest number
print(min(4, 8, 2, 9))             # Smallest number
print(sum([1, 2, 3, 4]))           # Sum of list
print(pow(5, 2))                   # Power function (5^2)
marks= [ 45, 50, 65, 80 ]
print(sorted(marks))                # Sort numbers in ascending order
print(sorted(marks, reverse=True))  # Sort numbers in descending order  
print(len(marks))                   # Get the number of elements in the list


'''User defined Funcitons: It is defined using the def keyword, followed by a function name and parentheses.
It helps you reuse code, organize logic, and avoid repetition.'''

def greet():
  print("Hello from a function")
greet()

# temprature conversion from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return statment is used to send data back from a function to the caller.
def greeting():
   return 'Hello'
print(greeting())

# Functions cannot be empty, but if you for some reason have a function without any code, use pas statment
def my_function():
  pass

# Function with parameters
def my_function(fname, lname):
  print(f'{fname} {lname}')
my_function("Ayesha", "Malik")

# Default parameter value , if no argument is provided, it uses the default value
def my_function(country= "Pakistan"):
  print("I am from " + country)
my_function()

# calling sum function inside avg function
def sum(x, y):
    return x + y
def avg():
   return sum(15, 30) / 2
print(avg())

#args parameter allows a function to accept any number of positional arguments
def my_function(*name):
   for n in name:            # use a for loop to iterate through the tuple of names
     print("Hello " + n)

my_function("Rabeea", "Areeba", "Qirat")

# function with conditional statements
x= int(input("Enter an integer number: "))            # Get user input 
def number(x):
    if x > 0:
        return x
    else:
        return 0

print(number(x))  # Output: 0

# if we assign a value to a variable outside a function, that variable is global variable and it accessible everywhere
x= 500
def my_func():
   print(x)

my_func()

# If we use the global keyword, the variable belongs to the global scope

def myfunc():
  global x
  x = 300
  print(x)

myfunc()          # both give output 300, because they both accesing the same global variable x
print(x)    

#decorators is a special type of function that modifies the behavior of another function.
def greet(fx):
   def mfx(*args):   #args allows the decorator to accept any number of arguments
      print("Good Morning")
      fx(*args)
      print("Have a nice day!")
   return mfx

@greet
def func():
   print("Hello World")

func()  # Calling func will also call greet due to the decorator

@greet
def another_func():
   print("Welcome to Python Functions")
another_func()  # Calling another_func will also call greet due to the decorator

@greet
def add(x, y):
    print(x + y)
add(5, 7)  

def num(x):
    return x * 2
print(num(5)) 

''' lambda function is a small anonymous function.
It can take any number of arguments, but can only have one expression.'''
 
num1= lambda x: x*2
print(num1(5))

num2= lambda x,y, z: x + y + z
print(num2(5, 10, 15))

cube= lambda x: x**3
print(cube(4))

avg= lambda x, y: (x + y) / 2
print(avg(10, 20))

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))  # Using map to apply lambda function to each element
print(result)


# Recursion: A function that calls itself is known as a recursive function.
def factorial(n):
   if ( n== 0 or n == 1):
       return 1
   else:
      return n * factorial(n-1)    #recursive call
print(factorial(3))
print(factorial(5))
print(factorial(7))

'''enerators allow you to iterate over data without storing the entire dataset in memory.
Instead of using return, generators use the yield keyword.'''

def my_generator():
   for i in range(15):
      yield i 
gen = my_generator()

# using a for loop to iterate through all values produced by the generator
for value in gen:
   print(value)