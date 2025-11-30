import pandas as pd

gl_balances = {
    'Accounts Receivable': 100000,
    'Accounts Payable': 50000,
    'Inventory': 75000
}

sl_balances = {
    'AR_Aging_Total': 98000,    
    'AP_Aging_Total': 50000,    
    'Inventory_Valuation': 75000 
}

print("--- RECONCILIATION DASHBOARD ---")
print(f"{'Account':<20} | {'GL Balance':<10} | {'SL Balance':<10} | {'Variance':<10} | {'Status'}")
print("-" * 75)

checks = [
    ('Accounts Receivable', gl_balances['Accounts Receivable'], sl_balances['AR_Aging_Total']),
    ('Accounts Payable',    gl_balances['Accounts Payable'],    sl_balances['AP_Aging_Total']),
    ('Inventory',           gl_balances['Inventory'],           sl_balances['Inventory_Valuation'])
]

for name, gl, sl in checks:
    var = gl - sl
    status = "✅ OK" if var == 0 else "❌ ERROR"
    print(f"{name:<20} | ${gl:<9} | ${sl:<9} | ${var:<9} | {status}")

print("-" * 75)
if any(c[1] != c[2] for c in checks):
    print("\n⚠️ DIAGNOSTIC: AR is off by $2,000.")
    print("Common Causes: A Journal Entry was posted directly to the AR GL account (Manual Adjustment).")
    print("Action: Run a 'GL Dump' on AR and filter for type 'Journal Entry'. Reverse it.")