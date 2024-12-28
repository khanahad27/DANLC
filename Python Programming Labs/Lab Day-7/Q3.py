#3.Python program to check if a given number is an Armstrong number.
#Taking input from the User.
num = int(input("Enter a number to check if it is an Armstrong number: "))
# Convert the number to a string to find the number of digits
num_str = str(num)
num_digits = len(num_str)
# Calculate the sum of digits raised to the power of the number of digits
sum_of_powers = 0
#Loop to check the condition
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
# Check if the number is an Armstrong number
if num == sum_of_powers:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
