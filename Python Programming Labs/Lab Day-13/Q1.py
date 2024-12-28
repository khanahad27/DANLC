#1.Write a Python program and calculate the mean of the below dictionary.
#Initializing the list
D = {"A":6,"B":9,"C":5,"D":7,"E":4}
#Calculating the mean
mean_value = sum(D.values()) / len(D)
#Output
print(f"Mean of the dictionary values: {mean_value}")