#2.Python program to check if the given string is a palindrome.
#Taking input From the User
input = str(input("Enter the string:"))
length = len (input)
is_palindrome = True
#Loop to check whether the string is palindrome or not.
for i in range(length//2):
    if input[i] != input[length - i - 1]:
        is_palindrome = False
        break
#Printing the Output
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

