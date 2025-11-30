import pandas as pd

crm_data = {
    'Employee_ID': ['E001', 'E002', 'E003'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Deals_Closed': [15, 8, 20],
    'Revenue_Generated': [150000, 80000, 200000]
}

ops_data = {
    'Employee_ID': ['E001', 'E002', 'E003'],
    'Tickets_Resolved': [120, 50, 80],
    'Avg_Response_Time_Mins': [30, 120, 45] 
}

hr_data = {
    'Employee_ID': ['E001', 'E002', 'E003'],
    'Days_Absent': [1, 5, 0] 
}

df_crm = pd.DataFrame(crm_data)
df_ops = pd.DataFrame(ops_data)
df_hr = pd.DataFrame(hr_data)

df_master = df_crm.merge(df_ops, on='Employee_ID').merge(df_hr, on='Employee_ID')

df_master['Rev_Per_Ticket'] = df_master['Revenue_Generated'] / df_master['Tickets_Resolved']

print("--- CONSOLIDATED MASTER DATA ---")
print(df_master.to_string(index=False))

df_master.to_csv("Master_KPI_Dataset.csv", index=False)