#Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
#Initializing the num
total_sum = 0
while True:
    num = int(input("Enter a number (enter 0 to stop):"))
    if num == 0:
        break
    total_sum += num
print("The sum of all numbers entered is:",total_sum)