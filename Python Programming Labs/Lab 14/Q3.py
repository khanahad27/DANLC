#3.Write a Python program to calculate the sum of the numbers in a given tuple. 
#Initializing the tuple
T = [(1, 2), (3, 4), (5, 6)]
#Calculating the sum
total_sum = sum(sum(tup) for tup in T)
print(f"The sum of numbers in the given list of tuples is {total_sum}.")

