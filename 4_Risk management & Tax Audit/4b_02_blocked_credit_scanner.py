import pandas as pd

ledger = pd.DataFrame({
    'Tx_ID': ['TX1', 'TX2', 'TX3', 'TX4', 'TX5'],
    'Category': ['Travel', 'Staff Welfare', 'Marketing', 'Repairs', 'Gifts'],
    'Description': [
        'Flight to NY', 
        'Lunch for team', 
        'Google Ads', 
        'Office Painting', 
        'Rolex watch for Director' 
    ],
    'Tax_Claimed': [500, 200, 1000, 300, 2000]
})

blacklist = ['food', 'lunch', 'dinner', 'restaurant', 'gift', 'personal', 'club', 'membership', 'spa', 'gym']

def check_eligibility(text):
    text = text.lower()
    for word in blacklist:
        if word in text:
            return f"BLOCKED ({word})"
    return "Eligible"

ledger['Status'] = ledger['Description'].apply(check_eligibility)

blocked = ledger[ledger['Status'].str.contains("BLOCKED")]

print("--- BLOCKED CREDIT SCANNER ---")
if not blocked.empty:
    print(f"🚫 ILLEGAL CLAIMS FOUND: {len(blocked)}")
    print(f"Total Risk Reversal: ${blocked['Tax_Claimed'].sum():,.0f}")
    print(blocked[['Category', 'Description', 'Tax_Claimed', 'Status']].to_string(index=False))
    
    print("\nAdvisory: Reclassify these tax amounts to 'Cost' (Expenses) instead of 'Input Tax Asset'.")
else:
    print("✅ No blocked keywords found.")