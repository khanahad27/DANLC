#Write a Python program to reverse words in a string.
#Initializig the string
String = "Deeptech Python Training"
print("Before:",String)
#Implementing the logic
reversed_string = ' '.join(reversed(String.split()))
#Printing the outcome
print("After:",reversed_string)