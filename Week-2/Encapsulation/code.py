''' Encapsulation means protecting the class data like it's attributes and methods
from being accessed directly from outside the class. This is done by making the attributes and methods private.'''

class Person:
    def __init__(self, name, age):
        self.name= name
        self.__age= age

# getter method to get the value of private attribute         
    def get_age(self):  
        return self.__age
    
# setter method to set or change teh value of the private attribute
    def set_age(self, age):
        if age>= 0:
            self.__age=age
        else:
            print("Age cannot be negative")

p1= Person("Sania", 21)
print(p1.name) 
try:
    print(p1.self.__age)   # it will give error because __age is private attribute
except:
    print("AttributeError: 'Person' object has no attribute 'self.__age'")
print(p1.get_age())
p1.set_age(25)
print(p1.get_age())

class BankAccount:
   
