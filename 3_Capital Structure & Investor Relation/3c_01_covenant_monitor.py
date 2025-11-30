import pandas as pd

financials = {
    'EBITDA': 1200000,
    'Total_Debt': 3800000,
    'Cash': 150000,
    'Principal_Payments': 200000,
    'Interest_Expense': 180000,
    'Current_Assets': 600000,
    'Current_Liabilities': 500000
}

covenants = {
    'Max_Leverage': {'Limit': 3.0, 'Type': 'Max'},   
    'Min_DSCR':     {'Limit': 1.25, 'Type': 'Min'},  
    'Min_Liquidity':{'Limit': 250000, 'Type': 'Min'} 
}

leverage = financials['Total_Debt'] / financials['EBITDA']

debt_service = financials['Principal_Payments'] + financials['Interest_Expense']
dscr = financials['EBITDA'] / debt_service

liquidity = financials['Cash']

results = {
    'Max_Leverage': leverage,
    'Min_DSCR': dscr,
    'Min_Liquidity': liquidity
}

print("--- BANK COMPLIANCE CHECK ---")
status = "PASS"

for metric, rule in covenants.items():
    actual = results[metric]
    limit = rule['Limit']
    
    is_fail = False
    if rule['Type'] == 'Max' and actual > limit: is_fail = True
    if rule['Type'] == 'Min' and actual < limit: is_fail = True
    
    is_warning = False
    if rule['Type'] == 'Max' and actual > (limit * 0.9): is_warning = True
    if rule['Type'] == 'Min' and actual < (limit * 1.1): is_warning = True

    flag = "✅ OK"
    if is_warning: flag = "⚠️ WARNING"
    if is_fail: 
        flag = "🚨 FAIL"
        status = "FAIL"
    
    print(f"{metric}: Actual {actual:.2f} | Limit {limit} | {flag}")

if status == "FAIL":
    print("\nACTION REQUIRED: You are in TECHNICAL DEFAULT.")
    print("Strategy: Do not submit this to the bank yet. We must inject capital or reclassify debt immediately.")