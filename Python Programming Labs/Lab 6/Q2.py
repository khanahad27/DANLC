#Write a python program to check whether a number is palindrome or not. 
#Takin input from the user.
num = int(input("Enter a number:"))
original_num = num
reversed_num = 0 
#Loops to check the number is a palindrome or not.
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
#Check if the original num is equal to reversed num
if original_num  == reversed_num:
    print(original_num,"is a palindrome.")
else:
    print(original_num,"is not a palindrome.")
