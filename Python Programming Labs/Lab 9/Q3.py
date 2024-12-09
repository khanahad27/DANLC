#
#Initializing the input and variables
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, numbers, special = 0, 0, 0, 0
#Loops to count uppercase, lowercase, digits and special character.
for char in input_str:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        special += 1
#printing the outcomes.
print(f"UpperCase : {uppercase}")
print(f"LowerCase : {lowercase}")
print(f"NumberCase : {numbers}")
print(f"SpecialCase : {special}")