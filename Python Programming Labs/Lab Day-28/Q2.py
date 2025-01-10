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
#Group by School Code and Calculate Mean, Min, Max for Age
school_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
#Display Result
print("Original data:")
print(student_data)
print("Age statistics by school code:")
print(school_stats)
#Horizontal Bar Chart
school_stats.plot(kind='barh', title='Age Statistics by School Code', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.xlabel('Age')
plt.ylabel('School Code')
plt.legend(['Mean Age', 'Min Age', 'Max Age'])
plt.show()



