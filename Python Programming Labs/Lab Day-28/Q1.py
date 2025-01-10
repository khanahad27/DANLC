#Importing the Pandas and Matplotlib library
import pandas as pd
import matplotlib.pyplot as plt
#Input Data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})
#Group by Class and Count Students
class_count = student_data.groupby('class').size()
#Display Result
print("Original data:")
print(student_data)
print("Number of students in each class:")
print(class_count)
#Bar Chart
class_count.plot(kind='bar', color='skyblue', title='Number of Students by Class')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()



