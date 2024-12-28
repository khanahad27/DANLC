#
#Initializing the inputs
input_str = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
#Implementing conditions.
count = sum(1 for char in input_str if char in vowels)
print(f"Total vowels are: {count}")
