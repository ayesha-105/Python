#creating class
class student:
    uniname= "SMIU"

#creating objects
s1= student()
s2= student()
print(s1.uniname)  # We acces our class variable using object
del s2   #deleting object s2
print(s2.uniname)  # this will give error as s2 is deleted

class Person:
    pass

p1= Person()
print(p1)