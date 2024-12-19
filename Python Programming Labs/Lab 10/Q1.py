#1.Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
#Accessing the file
with open("C:\\Users\\khana\\OneDrive\\Desktop\\DANLC Python Programming\\Lab 10\\ABC.txt","r") as file:
#Using for-loop to print lines from the file.
        for line in file:
            print(line.strip())