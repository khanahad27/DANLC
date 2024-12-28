#2.Write a Python program to Return a set of elements present in Set A or B, but not both.
#Initializing the sets 
# Input sets
S1 = {10, 20, 30, 40, 50}
S2 = {30, 40, 50, 60, 70}
#Elements in S1 or S2 but not both
symmetric_diff = S1.symmetric_difference(S2)
print(f"Elements in Set A or B but not both: {symmetric_diff}")

