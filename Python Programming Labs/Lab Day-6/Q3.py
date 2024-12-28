#Write a python program finding the factorial of a given number using a while loop. 
#Taking input from the user.
num = int(input("Enter a number:"))
factorial = 1
#Checking whether the number is negative or not.
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    #Loops to Calculate the factorial of the number.
    while num > 0:
        factorial *= num
        num -= 1
    print("Factorial is",factorial)