#1. Write a Python program to Get Only unique items from two sets.               
#Initializing the sets
S1 = {10, 20, 30, 40, 50}
S2 = {30, 40, 50, 60, 70}
#Fetching unique items from both sets
unique_items = S1.symmetric_difference(S2)
print(f"Unique items from both sets: {unique_items}")


