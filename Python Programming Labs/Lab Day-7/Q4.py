#4.Python program to get the Fibonacci series between 0 to 50 
#Initializing input
a, b = 0, 1
print("Fibonacci series between 0 and 50:")
#Loop to implement the condition
for _ in range(50):
    if a > 50:
        break
    print(a, end=" ")
    a, b = b, a + b
