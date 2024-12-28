#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number. 
#Taking Input From the user
x = int(input("Enter the number: "))
#Definig the Function
def square(x):                             
    return x * x
print("Square:",square(x))