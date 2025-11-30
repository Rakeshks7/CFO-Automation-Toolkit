import pandas as pd

invoice_lines = [
    {'Role': 'Junior Assoc', 'Hours': 10, 'Rate_Billed': 150}, 
    {'Role': 'Senior Assoc', 'Hours': 5,  'Rate_Billed': 350}, 
    {'Role': 'Partner',      'Hours': 2,  'Rate_Billed': 600}  
]

contract_rates = {
    'Junior Assoc': 150,
    'Senior Assoc': 300,
    'Partner': 600
}

df = pd.DataFrame(invoice_lines)

df['Contract_Rate'] = df['Role'].map(contract_rates)
df['Variance'] = df['Rate_Billed'] - df['Contract_Rate']
df['Overcharge'] = df['Variance'] * df['Hours']

errors = df[df['Variance'] > 0]

print("--- RATE AUDIT REPORT ---")
if not errors.empty:
    total_over = errors['Overcharge'].sum()
    print(f"🚫 OVERCHARGE DETECTED: ${total_over:,.2f}")
    print(errors[['Role', 'Rate_Billed', 'Contract_Rate', 'Overcharge']].to_string(index=False))
    
    print("\nAction: Reject invoice. Request credit note for the difference.")
else:
    print("✅ All rates match the master agreement.")