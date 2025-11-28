import calculator as calc

print( " Welcome to the Calculator")
a=float(input(" Enter first number: "))
b=float(input(" Enter second number: "))

print(" Select operation:")
print(" 1. Add")
print(" 2. Subtract")
print(" 3. Multiply")
print(" 4. Divide")
print(" 5. Power")
print(" 6. Modulus")

choice = input(" Enter choice 1 - 6 : ")
if choice == '1':
    print(f"{a} + {b} = {calc.add(a, b)}")
elif choice == '2':
    print(f"{a} - {b} = {calc.subtract(a, b)}")
elif choice == '3':
    print(f"{a} * {b} = {calc.multiply(a, b)}")
elif choice == '4':
    result = calc.divide(a, b)
    if result is not None:
        print(f"{a} / {b} = {result}")
elif choice == '5':
    print(f"{a} ^ {b} = {calc.power(a, b)}")        
elif choice == '6':
    print(f"{a} % {b} = {calc.modulus(a, b)}")
else:
    print(" Invalid input")

