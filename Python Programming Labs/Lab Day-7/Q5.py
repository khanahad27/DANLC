#5.Python program to check the validity of password input by users.
#Taking password from the user
password = input("Enter a password to check its valid or not: ")
#Initializing validation conditions
upper = False
lower = False
digit = False
special = False
special_char = "!@#$%^&*()-_+=<>?"
#Loop to implement the condition
for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    elif char in special_char:
        special = True
#Check the length of the password
length = len(password) >= 8
#Validating the password
if upper and lower and digit and special and length:
    print("The password is valid.")
else:
    print("The password is invalid.")
