import pandas as pd

financials = {
    'Revenue': 1200000,
    'COGS': 800000,
    'Avg_Inventory': 100000,
    'Avg_Accounts_Receivable': 150000,
    'Avg_Accounts_Payable': 80000
}

dio = (financials['Avg_Inventory'] / financials['COGS']) * 365

dso = (financials['Avg_Accounts_Receivable'] / financials['Revenue']) * 365

dpo = (financials['Avg_Accounts_Payable'] / financials['COGS']) * 365

ccc = dio + dso - dpo

print("--- WORKING CAPITAL DIAGNOSTIC ---")
print(f"1. Inventory Days (DIO): {dio:.0f} days")
print(f"2. Collection Days (DSO): {dso:.0f} days")
print(f"3. Payment Days (DPO):    {dpo:.0f} days")
print("-" * 30)
print(f"CASH CONVERSION CYCLE: {ccc:.0f} Days")
print("-" * 30)

if ccc > 60:
    print("⚠️ ADVISORY: Your cash is trapped too long. Strategies:")
    print("   - Offer 2% discount for early payment (reduce DSO)")
    print("   - Renegotiate vendor terms to Net-45 (increase DPO)")
elif ccc < 0:
    print("✅ ELITE STATUS: Negative Cash Cycle. You get paid before you pay suppliers (like Amazon).")