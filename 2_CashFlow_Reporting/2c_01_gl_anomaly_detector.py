import pandas as pd
from datetime import timedelta

data = {
    'Tx_ID': ['TX101', 'TX102', 'TX103', 'TX104', 'TX105', 'TX106', 'TX107'],
    'Date':  ['2025-11-03', '2025-11-05', '2025-11-05', '2025-11-09', '2025-11-12', '2025-11-12', '2025-11-20'],
    'Vendor':['Office Depot', 'Consultant X', 'Consultant X', 'Amazon', 'Supplier A', 'Supplier A', 'Contractor Z'],
    'Amount':[123.45,         5000.00,        5000.00,        450.00,     12500.00,     12500.00,     3000.00],
    'User':  ['Admin',        'CFO',          'CFO',          'Staff',    'Admin',      'Admin',      'Staff']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

suspicious_flags = []

df['Is_Weekend'] = df['Date'].dt.dayofweek.isin([5, 6])
weekends = df[df['Is_Weekend'] == True]
for idx, row in weekends.iterrows():
    suspicious_flags.append({'Tx_ID': row['Tx_ID'], 'Risk': 'Weekend Posting', 'Details': f"Posted on {row['Date'].day_name()}"})

dupes = df[df.duplicated(subset=['Vendor', 'Amount'], keep=False)]
ids_seen = set()
for idx, row in dupes.iterrows():
    if row['Tx_ID'] not in ids_seen:
        suspicious_flags.append({'Tx_ID': row['Tx_ID'], 'Risk': 'Duplicate Payment', 'Details': f"Match found for ${row['Amount']}"})
        ids_seen.add(row['Tx_ID'])

for idx, row in df.iterrows():
    if row['Amount'] > 1000 and row['Amount'] % 100 == 0:
        suspicious_flags.append({'Tx_ID': row['Tx_ID'], 'Risk': 'Round Number', 'Details': f"Exact amount: ${row['Amount']:.2f}"})

report = pd.DataFrame(suspicious_flags)
if not report.empty:
    final = report.merge(df[['Tx_ID', 'Vendor']], on='Tx_ID', how='left')
    print("--- GL AUDIT EXCEPTIONS ---")
    print(final[['Tx_ID', 'Vendor', 'Risk', 'Details']].to_string(index=False))
    
    final.to_csv("Audit_Exceptions.csv", index=False)
else:
    print("✅ No anomalies detected.")