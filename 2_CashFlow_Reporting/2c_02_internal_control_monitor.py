import pandas as pd

v1_data = {
    'Vendor_ID': ['V001', 'V002', 'V003'],
    'Name': ['Alpha Corp', 'Beta Ltd', 'Gamma Inc'],
    'Bank_Acct': ['123-456', '987-654', '555-555']
}

v2_data = {
    'Vendor_ID': ['V001', 'V002', 'V004'],
    'Name': ['Alpha Corp', 'Beta Ltd', 'Delta LLC'],
    'Bank_Acct': ['123-456', '111-222', '999-999'] 
}

df_old = pd.DataFrame(v1_data)
df_new = pd.DataFrame(v2_data)

merged = pd.merge(df_old, df_new, on='Vendor_ID', how='outer', suffixes=('_OLD', '_NEW'), indicator=True)

print("--- INTERNAL CONTROL REPORT ---")

new_vendors = merged[merged['_merge'] == 'right_only']
if not new_vendors.empty:
    print(f"\n[+] NEW VENDORS ADDED ({len(new_vendors)}):")
    print(new_vendors[['Vendor_ID', 'Name_NEW']].to_string(index=False))
    print("ACTION: Verify W-9 forms are on file for these.")

existing = merged[merged['_merge'] == 'both'].copy()
frauds = []

for idx, row in existing.iterrows():
    if row['Bank_Acct_OLD'] != row['Bank_Acct_NEW']:
        frauds.append({
            'Vendor': row['Name_NEW'],
            'Old_Bank': row['Bank_Acct_OLD'],
            'New_Bank': row['Bank_Acct_NEW']
        })

if frauds:
    print(f"\n🚨 CRITICAL SECURITY ALERT: BANK DETAILS CHANGED ({len(frauds)})")
    for f in frauds:
        print(f"  - {f['Vendor']}: Changed from {f['Old_Bank']} to {f['New_Bank']}")
    print("ACTION: Call vendor immediately to confirm. Do not process payments.")
else:
    print("\n✅ No changes to existing bank details.")