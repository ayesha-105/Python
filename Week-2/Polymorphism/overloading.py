''' Overloading: This a way to define multiple behaviors for a single function or operator based 
on the context in which it is used. In Python, operator overloading allows you to define how operators 
like + - * etc. behave for user-defined classes.'''

class Vector:
    def __init__(Self, i, j, k):
        Self.i = i
        Self.j = j
        Self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    
       
v1= Vector(2, 3, 4)
print(v1)
v2= Vector(5, 6, 7)
print(v2)
print(v1 + v2)

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):  
        return f"{self.real} + {self.imag}i"
    
    def __add__(self, x):
        return complex(self.real + x.real, self.imag + x.imag)
    
    def __sub__(self, y):
        return complex(self.real - y.real, self.imag - y.imag)

    
c1 = complex(2, 3)
c2 = complex(5, 6) 
print(c1)
print(c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
    