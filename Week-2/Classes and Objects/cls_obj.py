#creating class
class student:
    uniname= "SMIU"

#creating objects
s1= student()
s2= student()
print(s1.uniname)  # We acces our class variable using object

#deleting object s2
del s2  
try:
    print(s2.uniname)  # this will give error as s2 is deleted
except:
    print("The object s2 is deleted and cannot be accessed")

# class cannot be empty but if we want to create empty class for some reason, we use pass statemnt to avoid error
class Person:
    pass

