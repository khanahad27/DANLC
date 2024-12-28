#3.Python Program to Check if a Number is Positive, Negative or 0.
#Taking the input from the user
x = int(input("Enter the number: "))
#Applying logic
if x > 0:
    print(x,"is a positive integer.")
elif x < 0:
    print(x,"is a negative integer.")
else:
    print("The number you entered is zero.")