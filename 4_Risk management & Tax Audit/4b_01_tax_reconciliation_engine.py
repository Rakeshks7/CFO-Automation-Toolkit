import pandas as pd

my_books = pd.DataFrame({
    'Invoice_No': ['INV-101', 'INV-102', 'INV-103', 'INV-104'],
    'Vendor': ['Vendor A', 'Vendor B', 'Vendor C', 'Vendor D'],
    'Tax_Amount': [1000, 2500, 500, 1200]
})

govt_data = pd.DataFrame({
    'Invoice_No': ['INV-101', 'INV-102', 'INV-103-REV'], 
    'Vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
    'Tax_Available': [1000, 2500, 500]
})

merged = pd.merge(my_books, govt_data, on='Invoice_No', how='left', indicator=True)

missing_in_govt = merged[merged['_merge'] == 'left_only']

print("--- TAX CREDIT RECONCILIATION ---")
print(f"Total Claim in Books: ${my_books['Tax_Amount'].sum():,.0f}")
print(f"Total Matched:        ${merged[merged['_merge']=='both']['Tax_Amount'].sum():,.0f}")
print("-" * 40)

if not missing_in_govt.empty:
    print(f"⚠️ MISMATCH DETECTED: ${missing_in_govt['Tax_Amount'].sum():,.0f} is at risk.")
    print("These vendors have NOT filed their returns (or invoice numbers don't match):")
    print(missing_in_govt[['Vendor_x', 'Invoice_No', 'Tax_Amount']].to_string(index=False))
    
    print("\nACTION: Email these vendors immediately. Do not pay their next bill until they file.")