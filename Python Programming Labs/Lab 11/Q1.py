#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
#Implementing try and except block
try:
#Initializing the input
    num = int(input("Enter the number:"))
    result = num / 0
except ZeroDivisionError:
#Exception
    print("You cannot divide by zero!")


