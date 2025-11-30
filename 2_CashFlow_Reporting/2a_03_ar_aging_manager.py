import pandas as pd
from datetime import datetime

today = pd.to_datetime('2024-11-29')

data = {
    'Invoice': ['INV-001', 'INV-002', 'INV-003', 'INV-004', 'INV-005'],
    'Client': ['Client A', 'Client B', 'Client C', 'Client D', 'Client E'],
    'Due_Date': ['2024-11-28', '2024-10-15', '2024-11-10', '2024-08-01', '2024-11-20'],
    'Amount': [5000, 12000, 3000, 15000, 2000]
}
df = pd.DataFrame(data)
df['Due_Date'] = pd.to_datetime(df['Due_Date'])

df['Days_Overdue'] = (today - df['Due_Date']).dt.days

def get_bucket(days):
    if days <= 0: return 'Current'
    elif days <= 30: return '1-30 Days'
    elif days <= 60: return '31-60 Days'
    elif days <= 90: return '61-90 Days'
    else: return '90+ Days (Critical)'

df['Status'] = df['Days_Overdue'].apply(get_bucket)

collection_list = df[df['Days_Overdue'] > 0].sort_values(by='Amount', ascending=False)

print(f"--- COLLECTION CALL LIST ({today.date()}) ---")
print(collection_list[['Client', 'Amount', 'Days_Overdue', 'Status']].to_string(index=False))

total_overdue = collection_list['Amount'].sum()
print(f"\nTOTAL CASH STUCK IN AR: ${total_overdue:,.0f}")