#2.Write a Python program to get the largest and smallest number from a list without builtin functions.
#Initializing List and variables
L2 = [5,10,15,20,25,30]
largest = L2[0]
smallest = L2[0]
for a in L2:
    if a > largest:
        largest = a
    if a < smallest:
        smallest = a
print("Largest number:", largest)
print("Smallest number:", smallest)


