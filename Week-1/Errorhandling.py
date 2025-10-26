a = input("Enter a number:")
print(f"Multiplication table of {a} is:")

try:                                               # for error handling using try and except block 
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
# except Exception as e:                         # this will handle error and print the error message
#      print(e)
except:                                          # this will handle error and print a custom message
    print(" some error occured")

print("Program ended successfully.")