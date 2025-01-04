#Importing the Pandas library
import pandas as pd
#Input data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
#Creating a Pandas Series
scores_series = pd.Series(exam_scores, index=students)
#Output
print("Exam Scores of Students:")
print(scores_series)



