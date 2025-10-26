# import os module to perform file operations like delete
import os    

f= open("D:\Coding\VS CODE\Python\Week-1\File Handling\myfile.txt","r")  #open takes two arguments filename and mode
print(f)                       # it returns a file object
print(f.read())                # it returns the content of the file as a string
f.close()                     # it closes the file                    

f1= open("myfile2.txt","w")  # open file in write mode
f1.write("Don't just dream it, \n")    # write string to the file
f1.write("Don't just think it,.\n")
f1.write("Make it happen!\n")
f1.close()               

# with statement is used for file handling, it automatically closes the file after the nested block of code
with open("myfile2.txt","r") as f2:  
     print(f2.read())       
         
with open("myfile2.txt","a") as f3:  # open file in append mode it adds content to the end of the file
        f3.write("Believe in yourself and all that you are.\n")

with open("myfile2.txt","r") as f4:
       print(f4.readline())      # it reads a single line from the file
       print(f4.readlines())     # it reads all the lines and returns a list of lines

with open("myfile2.txt", "r") as f5:
       for line in f5:
              print (line)            # iterating through each line in the file

with open("myfile3.txt", "w") as f6:
       f6.write("Content for myfile3.txt\n")

os.remove("myfile3.txt")  # it deletes the specified file