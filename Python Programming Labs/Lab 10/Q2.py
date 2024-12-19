#2.Write a function in Python to count and display the total number of words in a text file “ABC.txt”
#Accessing the file
with open("C:\\Users\\khana\\OneDrive\\Desktop\\DANLC Python Programming\\Lab 10\\ABC.txt", "r") as file:
#Fetching data from the file
    content = file.read()
    words = content.split()
    print("Total number of words:", len(words))