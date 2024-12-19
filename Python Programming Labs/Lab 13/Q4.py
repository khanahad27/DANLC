#4.Write a Python program to get the key, value and item in a dictionary. 
#Initializing the dictionary
D = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
#Using For-loop to get key, values and items
for key, value in D.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")