#4.Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
def display_words(filename):
    with open(filename,'r') as file:
        for line in file:
            words = line.split()  # Split line into words
            short_words = [word for word in words if len(word) < 4]  # Filter words less than 4 characters
            print(' '.join(short_words))
# Example usage:
display_words("C:\\Users\\khana\\OneDrive\\Desktop\\DANLC Python Programming\\Lab 10\\story.txt")
