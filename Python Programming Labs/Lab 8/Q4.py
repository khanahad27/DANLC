#Write a Python program to count and display the vowels of a given text.
#Initializing the String
String = "Welcome to python Training"
#Declaring the String
vowels = "aeiou"
vowel_count = {v: 0 for v in vowels}
#Loop to count the vowels in the text
for char in String.lower():
    if char in vowels:
        vowel_count[char] += 1
#Printing the vowel's count
print(vowel_count)
