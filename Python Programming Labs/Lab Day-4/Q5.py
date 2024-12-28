#5.Write a python program to calculate the transport distance entered by user.
#Taking the input from the user
distance = int(input("Enter the distance:"))
charges = float
amount = 0
#Applying the conditions
if distance >=1 and distance <=50:
    amount = distance * 8
    print("The amount for",distance,"km is",amount)
elif distance >=51 and distance <=100:
    amount = distance * 10
    print("The amount for",distance,"km is",amount)
elif distance > 100:
    amount = distance * 12
    print("The amount for",distance,"km is",amount)
else:
    print("Invalid Input.")
    