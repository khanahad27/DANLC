#2.Write a Python script to concatenate the following dictionaries to create a new one.
#Initializing the dictionaries
D1 = {1: 10, 2: 20}
D2 = {3: 30, 4: 40}
D3 = {5: 50, 6: 60}
#COncatenating all the dictionary into one
final_dict = {**D1, **D2, **D3}
#Output
print(f"Concatenated dictionary: {final_dict}")
