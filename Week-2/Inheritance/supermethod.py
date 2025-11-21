class Car:
    def __init__(self, car_type):
        self.car_type= car_type
        print(f"car type is {self.car_type}")

    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("car stopped")

class SUZUKI(Car):
    def __init__(self, model, car_type):
        super().__init__(car_type)
        self.model= model
        print(f"car model is {self.model}")
    
    def showdetails(Self):
        super().start()
        print(f"Car is going with 80 km/h speed")
        super().stop()

s1= SUZUKI("Alto", "Automatic")
s1.showdetails()