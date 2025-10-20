'''In Python, a function is defined using the def keyword, followed by a function name and parentheses.
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