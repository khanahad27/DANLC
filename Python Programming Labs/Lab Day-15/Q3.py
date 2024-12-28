#3.Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
#Initializing the sets
S1 = {10, 20, 30, 40, 50}
S2 = {60, 70, 80, 90, 10}
#Finding common elements
common_elements = S1.intersection(S2)
if common_elements:
    print(f"Common elements: {common_elements}")
else:
    print("No common elements found.")


    
