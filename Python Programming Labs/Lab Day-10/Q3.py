#3.Write a function in Python to count uppercase character in a text file “ABC.txt”
#Accessing the file
with open("C:\\Users\\khana\\OneDrive\\Desktop\\DANLC Python Programming\\Lab 10\\ABC.txt", "r") as file:
#fetching the data from the file
    content = file.read()
    uppercase_count = sum(1 for char in content if char.isupper())
    print("Total uppercase characters:", uppercase_count)