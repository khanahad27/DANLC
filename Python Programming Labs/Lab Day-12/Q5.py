#5.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 
#Original list: ['red', 'green', 'white', 'black']
#Initializing List 
L5 = ['red', 'green', 'white', 'black']
#Using for-loop to traverse the list in the reverse order
for a in range(len(L5) -1, -1, -1):
    print(f"Index: {a}, Elements: {L5[a]}")

    