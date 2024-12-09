#Write a Python program to remove a newline in Python.
#Initializing the string
String = "\nBest \nDeeptech \nPython \nTraining\n"
print("Before formatting:",String)
#Formatting the sentence.
cleaned_string = String.replace('\n','').strip()
#Displaying the final output.
print("After formatting:",cleaned_string)