import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Master_KPI_Dataset.csv")

df['Score_Response'] = (df['Avg_Response_Time_Mins'].max() - df['Avg_Response_Time_Mins']) / (df['Avg_Response_Time_Mins'].max() - df['Avg_Response_Time_Mins'].min())
df['Score_Attendance'] = (df['Days_Absent'].max() - df['Days_Absent']) / (df['Days_Absent'].max() - df['Days_Absent'].min())

df['Score_Sales'] = (df['Revenue_Generated'] - df['Revenue_Generated'].min()) / (df['Revenue_Generated'].max() - df['Revenue_Generated'].min())

df['Total_Index'] = (df['Score_Sales']*0.5 + df['Score_Response']*0.3 + df['Score_Attendance']*0.2) * 100

heatmap_data = df[['Name', 'Total_Index', 'Score_Sales', 'Score_Response', 'Score_Attendance']].set_index('Name')

plt.figure(figsize=(8, 5))
sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', fmt=".1f", linewidths=.5)
plt.title("Employee Performance Normalization (0-1 Scale)")
plt.savefig("Employee_Performance_Matrix.png")
print("Heatmap generated.")
plt.show()