#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
#Implementing try and except block
try:
#Initializing the input
    user_input = input("Enter an integer: ")
    num = int(user_input)
except ValueError:
#Exception
    print("Invalid input! Please enter a valid integer.")



