#Importing the Pandas and Matplotlib library
import pandas as pd
import matplotlib.pyplot as plt
#Input Data
df = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', 
                 '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'],
    'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
})
#Convert 'ord_date' to datetime
df['ord_date'] = pd.to_datetime(df['ord_date'], format='%m-%d-%Y')
#Group by Customer ID and Calculate Total, Min, Mean, and Max Purchases
customer_purchases = df.groupby('customer_id')['purch_amt'].agg(['sum', 'min', 'mean', 'max']).reset_index()
#Display Result
print("Customer-wise Purchases (Total, Min, Mean, Max):")
print(customer_purchases)
#Bar Chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(customer_purchases['customer_id'] - 0.2, customer_purchases['sum'], width=0.2, label='Total Purchase', color='lightblue', edgecolor='black')
ax.bar(customer_purchases['customer_id'], customer_purchases['min'], width=0.2, label='Min Purchase', color='lightgreen', edgecolor='black')
ax.bar(customer_purchases['customer_id'] + 0.2, customer_purchases['mean'], width=0.2, label='Mean Purchase', color='lightcoral', edgecolor='black')
ax.bar(customer_purchases['customer_id'] + 0.4, customer_purchases['max'], width=0.2, label='Max Purchase', color='lightskyblue', edgecolor='black')
ax.set_title('Customer-wise Purchase Statistics (Total, Min, Mean, Max)')
ax.set_xlabel('Customer ID')
ax.set_ylabel('Purchase Amount')
ax.set_xticks(customer_purchases['customer_id'])
ax.set_xticklabels(customer_purchases['customer_id'])
ax.legend(title='Purchase Type')
plt.tight_layout()
plt.show()




