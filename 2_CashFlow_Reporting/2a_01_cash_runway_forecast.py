import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

start_date = '2024-11-01'
starting_cash = 50000
safety_buffer = 10000

monthly_rent = 5000  
biweekly_payroll = 15000 

transactions = [
    {'Date': '2024-11-05', 'Amount': 20000, 'Desc': 'Client A Payment'},
    {'Date': '2024-11-10', 'Amount': -8000, 'Desc': 'Server Costs'},
    {'Date': '2024-11-15', 'Amount': 15000, 'Desc': 'Client B Payment'},
    {'Date': '2024-11-20', 'Amount': -40000, 'Desc': 'Inventory Purchase'}, 
    {'Date': '2024-12-05', 'Amount': 25000, 'Desc': 'Client C Payment'}
]

dates = pd.date_range(start=start_date, periods=91)
df = pd.DataFrame(index=dates)
df['Daily_Net_Change'] = 0.0

df.loc[df.index.day == 1, 'Daily_Net_Change'] -= monthly_rent

payroll_dates = pd.date_range(start=start_date, periods=7, freq='14D')
for d in payroll_dates:
    if d in df.index:
        df.at[d, 'Daily_Net_Change'] -= biweekly_payroll

for t in transactions:
    t_date = pd.to_datetime(t['Date'])
    if t_date in df.index:
        df.at[t_date, 'Daily_Net_Change'] += t['Amount']

df['Ending_Balance'] = df['Daily_Net_Change'].cumsum() + starting_cash

min_balance = df['Ending_Balance'].min()
crunch_days = df[df['Ending_Balance'] < 0]

print("--- CASH FLOW FORECAST (13-WEEK) ---")
print(f"Starting Cash: ${starting_cash:,.0f}")
print(f"Lowest Point:  ${min_balance:,.0f}")

if not crunch_days.empty:
    first_fail = crunch_days.index[0].strftime('%Y-%m-%d')
    print(f"\n⚠️ CRITICAL WARNING: You run out of cash on {first_fail}!")
    print(f"Deficit: ${crunch_days.iloc[0]['Ending_Balance']:,.0f}")
else:
    print("\n✅ SAFE: Cash remains positive for 13 weeks.")

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Ending_Balance'], label='Projected Cash', color='green')
plt.axhline(0, color='red', linewidth=2, label='Bankruptcy Line')
plt.axhline(safety_buffer, color='orange', linestyle='--', label='Safety Buffer')

plt.fill_between(df.index, df['Ending_Balance'], 0, where=(df['Ending_Balance'] < 0), color='red', alpha=0.3)

plt.title('13-Week Cash Flow Forecast')
plt.ylabel('Cash Balance ($)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig("Cashflow_Forecast_Chart.png")
plt.show()