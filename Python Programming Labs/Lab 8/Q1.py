#Write a Python program to count the occurrences of each word in a given sentence.
#Initializing the string
string = "I am Abdul Ahad Khan from Bhiwandi, an aspiring developer loves to write code."
words = string.lower().split()
word_count = {}
#Loop to count the occurrence of each words
for word in words:
    word = word.strip('.')
    word_count[word] = word_count.get(word, 0) + 1
#Displaying the output
print(word_count)
