#
#Initializing the input
input_str = "String and String Function"
seen = set()
result = []
#Loops to remove duplicate characters.
for char in input_str:
    if char not in seen:
        seen.add(char)
        result.append(char)
#Printing the result
print("".join(result))
