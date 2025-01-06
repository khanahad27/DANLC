#Importing the Pandas and Numpy library
import pandas as pd
import numpy as np
#Input DataFrame
df = pd.DataFrame({
    'ord_no': [np.nan, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [np.nan, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': [np.nan, '2012-09-10', np.nan, '2012-08-17', '2012-09-10', 
                 '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', 
                 '2012-08-17', '2012-04-25'],
    'customer_id': [np.nan, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001]
})
#Original Dataframe
print(f"Original Dataframe:\n {df}")
# Drop rows where all elements are missing
cleaned_df = df.dropna(how='all')
print("DataFrame after dropping rows with all missing values:")
print(cleaned_df)



