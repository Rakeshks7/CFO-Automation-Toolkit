import pandas as pd
from datetime import datetime, timedelta

contracts = [
    {'Vendor': 'Salesforce', 'Expiry': '2026-03-31', 'Notice_Days': 60, 'Annual_Cost': 50000},
    {'Vendor': 'Office Rent', 'Expiry': '2026-06-30', 'Notice_Days': 180, 'Annual_Cost': 120000},
    {'Vendor': 'Cleaning Co', 'Expiry': '2026-01-15', 'Notice_Days': 30, 'Annual_Cost': 5000}
]
df = pd.DataFrame(contracts)
df['Expiry'] = pd.to_datetime(df['Expiry'])

today = pd.to_datetime('2025-12-01')

df['Last_Cancel_Date'] = df['Expiry'] - pd.to_timedelta(df['Notice_Days'], unit='D')
df['Days_Until_Lock'] = (df['Last_Cancel_Date'] - today).dt.days

urgent = df[(df['Days_Until_Lock'] >= 0) & (df['Days_Until_Lock'] <= 90)].copy()

print(f"--- RENEWAL WATCHDOG ({today.date()}) ---")

if not urgent.empty:
    print(f"🚨 ACTION REQUIRED: {len(urgent)} contracts are about to auto-renew!")
    print(urgent[['Vendor', 'Last_Cancel_Date', 'Days_Until_Lock', 'Annual_Cost']].to_string(index=False))
    
    print("\nAdvisory Script:")
    print("'Hi [Vendor], per our contract, we are approaching the renewal window.'")
    print("'We are currently reviewing alternative providers. Please send your best renewal offer.'")
else:
    print("✅ No immediate renewal risks.")