#
#Initializing the input and variables
input_str = "P@#yn26at^&i5ve"
chars, digits, symbols = 0, 0, 0
#Loops to count letters, digits and special symbols.
for char in input_str:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
#Printing the outcomes.
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")