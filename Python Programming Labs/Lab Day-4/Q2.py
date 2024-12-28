#2.Python Program to Find the Largest Among Three Numbers.
#Taking the input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
#Applying logic
if a > b and a > c:
    print(a,"is greater than",b,"&",c)
elif b > a and b > c:
    print(b,"is greater than",a,"&",c)
else:
    print(c,"is greater than",a,"&",c)

