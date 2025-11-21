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
    def __init__(self, brand, car_type):
        super().__init__(car_type)
        self.brand= brand
        print(f"car brand is {self.brand}")

    def feature(self):
        print("Suzuki brand cars have good fuel efficiency.")

class Alto(SUZUKI):
    def __init__(self, model, brand, car_type):
        super().__init__(brand, car_type)
        self.model=model
        print(f"car model is {self.model}")

# overriding start method it means reuse the meethod of parent class with some modification in child class
    def start(self):  
        print("Alto started silently with new ECO technology")

    def showdetails(self):
        super().start()
        print(f"Car is going with 80 km/h speed")
        super().stop()
        super().feature()
        self.start()

s1=Alto("ModelX", "Suzuki", "Automatic")
s1.showdetails()
    