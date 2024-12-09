#Write a python program to reverse a number using a while loop.
#Taking input from the user
num = int(input("Enter the Number:"))
#Initializing the reverse num
reverse_num = 0
#Loop to reverse the num
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
#printing the reversed numbers
print("Reversed Numbers:",reverse_num)
