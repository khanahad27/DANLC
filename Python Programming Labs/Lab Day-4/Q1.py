#1.Python program to check leap year.
#Taking input from the user.
Y = int(input("Enter the year: "))
if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
    print(Y,"is the Leap Year.")
else:
    print(Y,"is not the Leap Year.")
