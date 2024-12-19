#4.Write a python program and iterate the given tuples 
#Initializing the tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
#Iterating through the tuples
employees = [employee1, employee2, employee3]
for emp in employees:
    print(f"Name: {emp[0]}, ID: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}")

    
