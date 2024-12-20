#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
#Implementing try and except block
try:
#Initializing the input
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    result = int(num1) + int(num2)
    print(f"The result is {result}")
except ValueError:
#Exception
    print("Both inputs must be numerical values.")



