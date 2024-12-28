#4.Write a Python program to Remove items from set1 that are not common to both set1 and set2. 
#Initializing the sets
S1 = {10, 20, 30, 40, 50}
S2 = {30, 40, 50, 60, 70}
# Keep only items common to both sets
S1.intersection_update(S2)
print(f"Modified S1: {S1}")



