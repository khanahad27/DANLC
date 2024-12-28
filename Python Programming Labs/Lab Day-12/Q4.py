#4.Write a Python program to split a given list into two parts where the length of the first part of the list is given.
#Original list: [1, 1, 2, 3, 4, 4, 5, 1] 
#Initializing List and length 
L4 = [1,1,2,3,4,4,5,1]
n = 4
#Splitting the list into two parts
P1 = L4[:n]
P2 = L4[n:]
#Displaying the results.
print("First part:", P1)
print("Second part:", P2)

