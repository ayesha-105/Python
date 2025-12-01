'''default constructor all classes have a builtin constructor which is automatically called 
when we create object of that class''' 

class Person:
    name= "Ayesha Malik"
    def __init__(self):  
        print("This is default constructor")

p1= Person()           #it first print the print statement inside constructor
print(p1.name)         # then it print the name attribute of class Person

class Student:
    university= "SMIU"
    name= "Farah Malik"

    # parameterized constructor
    def __init__ (self, name, age):
        self.name= name
        self.age= age
       
    #instance method
    def welcome(self):
        print("Welcome to", self.university, self.name)       

s1= Student("Ayesha Malik", 20)
s2= Student("Areeba Imran", 22)
s1.welcome()
s2.welcome()

''' if class and obj attr has same same name, obj attr will be given preference becuase obj attr > class attr
that's why when we call welcome method it print obj attr name instead of class attr name '''

class Calculator:

    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def subtract(self, a, b):
        return a - b

    # Multiplication
    def multiply(self, a, b):
        return a * b

    # Division
    def divide(self, a, b):
        if b == 0:          # Zero division check
            return "Error: Cannot divide by zero!"
        return a / b
    
calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(50, 25))
print("Multiplication:", calc.multiply(5, 3))
print("Division:", calc.divide(10, 5))

# Decorators: These are also method of class but they are used to modify the behaviour of methods.

# we use s@taticmethod decorator when we don't want to use self parameter in method

class Student:
    @staticmethod
    def __hello(): #private method it can only be accessed inside the class
        print("Hello studnets")

    def welcome(self):
        self.__hello()

s1= Student()
s1.welcome()

# @classmethod decorator is bound to class not to object so we use cls parameter instead of self

class Person:
    name= "Ayesha Malik"
    
    @classmethod  
    def change_name(cls, name):
        cls.name= name

p1= Person()
p1.change_name("Areeba")  # it change the class attribute name
print(p1.name)            # it print the updated class attribute name


  


