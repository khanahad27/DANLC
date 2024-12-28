#3.Write a Python program to find duplicate values from a list and display those.
#Initializing List and variable
L3 = [1,2,2,3,4,5,5]
duplicates = []
#Using for-loop to find out duplicate values
for a in range(len(L3)):
     for b in range(a + 1, len(L3)):
          if L3[a] == L3[b] and L3[a] not in duplicates:
               duplicates.append(L3[a])
print("Duplicate values:",duplicates)

