'''Single inheritance means one child class derives properties and methods from one parent class.'''

class Car:
    type= "Automatic"
    
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("car stopped")

class SUZUKI(Car):
    def __init__(self, model):
        self.model= model
        print(f"Car model is {self.model}")

s1= SUZUKI("Alto")
print("Car type is", s1.type)
s1.start()  




     