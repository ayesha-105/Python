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

class Backaccount:
    def __init__(self, acc_number, balance):
        self.acc_number= acc_number
        self.__balance= balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            print(f"The amount {amount} is deposited. Current balance is {self.__balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"The amount {amount} is withdrawn. Remaining balance is {self.__balance}")
        else:
            print("Insufficient funds")
    

acc1= Backaccount("1001", 10000)
print("Account number: " , acc1.acc_number)
print("Current Balance: " , acc1.get_balance())
acc1.deposit(5000)
acc1.withdraw(2000)






