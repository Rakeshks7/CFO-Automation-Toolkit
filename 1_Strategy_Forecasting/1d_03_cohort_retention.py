import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Customer_ID': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4],
    'Transaction_Date': ['2024-01-01', '2024-02-01', '2024-03-01',
                         '2024-01-01', '2024-02-01',
                         '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01',
                         '2024-03-01']
}
df = pd.DataFrame(data)
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

df['OrderPeriod'] = df['Transaction_Date'].dt.to_period('M')
df['CohortGroup'] = df.groupby('Customer_ID')['Transaction_Date'].transform('min').dt.to_period('M')

cohorts = df.groupby(['CohortGroup', 'OrderPeriod']).agg({'Customer_ID': pd.Series.nunique})
cohorts.rename(columns={'Customer_ID': 'TotalUsers'}, inplace=True)

cohorts_flat = cohorts.reset_index()
cohorts_flat['CohortPeriod'] = cohorts_flat.groupby('CohortGroup').cumcount() + 1
cohorts = cohorts_flat

cohort_pivot = cohorts.pivot_table(index='CohortGroup', columns='CohortPeriod', values='TotalUsers')

cohort_size = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_size, axis=0)

plt.figure(figsize=(10, 6))
sns.heatmap(retention, annot=True, fmt='.0%', cmap='Blues', vmin=0.0, vmax=0.5)
plt.title('Cohort Analysis: Retention Rates')
plt.ylabel('Cohort Group (Join Date)')
plt.xlabel('Months Since Joining')
plt.savefig("Cohort_Analysis.png")
print("Cohort Chart generated.")
plt.show()