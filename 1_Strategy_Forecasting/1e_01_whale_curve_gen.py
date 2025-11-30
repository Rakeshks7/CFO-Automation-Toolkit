import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Customer': [f'Cust_{i}' for i in range(1, 11)],
    'Revenue': [100000, 80000, 95000, 20000, 15000, 40000, 12000, 50000, 30000, 5000],
    'Direct_Cost': [40000, 30000, 85000, 5000, 4000, 10000, 11000, 20000, 10000, 2000],
    'Allocated_Overhead': [10000, 5000, 5000, 2000, 1000, 2000, 4000, 5000, 2000, 8000] 
}
df = pd.DataFrame(data)

df['Net_Profit'] = df['Revenue'] - df['Direct_Cost'] - df['Allocated_Overhead']

df = df.sort_values(by='Net_Profit', ascending=False).reset_index(drop=True)

df['Cumulative_Profit'] = df['Net_Profit'].cumsum()
total_profit = df['Net_Profit'].sum()

df['Cum_Profit_Pct'] = df['Cumulative_Profit'] / total_profit
df['Customer_Pct'] = (df.index + 1) / len(df)

plt.figure(figsize=(10, 6))
plt.plot(df['Customer_Pct'], df['Cum_Profit_Pct'], marker='o', linewidth=2, color='#2980b9')

plt.axhline(1.0, color='green', linestyle='--', label='100% of Profit')
plt.axhline(df['Cum_Profit_Pct'].max(), color='red', linestyle=':', label='Peak Profit Potential')

plt.title('Customer Profitability "Whale Curve"')
plt.xlabel('% of Customers')
plt.ylabel('% of Total Profit')
plt.grid(True, alpha=0.3)
plt.legend()

peak_profit = df['Cumulative_Profit'].max()
lost_profit = peak_profit - total_profit
print(f"--- PROFITABILITY INSIGHTS ---")
print(f"Current Total Profit: ${total_profit:,.0f}")
print(f"Maximum Potential Profit: ${peak_profit:,.0f}")
print(f"⚠️ Value Destroyed by Unprofitable Customers: ${lost_profit:,.0f}")

plt.savefig("Whale_Curve_Analysis.png")
plt.show()

hit_list = df[df['Net_Profit'] < 0]
print("\n--- ACTION REQUIRED: RENEGOTIATE OR FIRE ---")
print(hit_list[['Customer', 'Revenue', 'Net_Profit']])
hit_list.to_csv("Unprofitable_Customers_List.csv")