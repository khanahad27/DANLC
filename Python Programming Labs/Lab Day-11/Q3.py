#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
#Implementing try and except block
try:
#Reading a file
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
#Exception
    print("The file does not exist.")



