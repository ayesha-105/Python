''' Ploymorphism using method overriding and method overloading.
Mthod overriding is like use a same method name in different classes with different implementations.'''

class Aniaml():
    def sound(Self):
        print("Animals make different sounds")

class Dog(Aniaml):
    def sound(self):
        print("Dog barks")

    def showdetails(self):
        super().sound()
        self.sound()
d= Dog()
d.showdetails()

class Car:
    def move(self):
       print("Car is Driving!")

class Boat:
    def move(self):
       print("Boat is Sailing!")

class Plane:
    def move(self):
        print("Plane is Flying!")

car1 = Car()
boat1 = Boat()     
plane1 = Plane()     

for x in (car1, boat1, plane1):
  x.move()

class Shape:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def area(self):
        print("Area of shape is", self.x * self.y)

class Circle(Shape):
    def __init__(Self, radius,x,y):
        super().__init__(x, y)
        Self.radius = radius

    def area(self):
        print("Area of circe is ", 3.14 * self.radius**2)

    def calculations(self):
        super().area()
        self.area()

c= Circle(7,4,5)
c.calculations()