import pandas as pd

invoices = [
    {'Inv_ID': 'INV-001', 'Currency': 'EUR', 'Amount': 50000, 'Booked_Rate': 1.08}, 
    {'Inv_ID': 'INV-002', 'Currency': 'GBP', 'Amount': 20000, 'Booked_Rate': 1.25},
    {'Inv_ID': 'INV-003', 'Currency': 'EUR', 'Amount': 10000, 'Booked_Rate': 1.08}
]
df = pd.DataFrame(invoices)

current_rates = {
    'EUR': 1.12,  
    'GBP': 1.22   
}

df['Current_Rate'] = df['Currency'].map(current_rates)

df['Booked_Cost_USD'] = df['Amount'] * df['Booked_Rate']
df['Current_Cost_USD'] = df['Amount'] * df['Current_Rate']
df['FX_Impact'] = df['Current_Cost_USD'] - df['Booked_Cost_USD']

total_impact = df['FX_Impact'].sum()

print("--- FX EXPOSURE REPORT ---")
print(df[['Inv_ID', 'Currency', 'Amount', 'Booked_Rate', 'Current_Rate', 'FX_Impact']].to_string(index=False))
print("-" * 40)

if total_impact > 0:
    print(f"⚠️ DANGER: Currency swings have increased your AP liability by ${total_impact:,.0f}.")
    print("Advisory: The USD is weakening against the Euro.")
else:
    print(f"✅ WIN: Currency swings have saved you ${abs(total_impact):,.0f}.")