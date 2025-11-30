debt_balance = 500000
equity_value = 1500000
cost_of_debt = 0.08    
cost_of_equity = 0.15  
tax_rate = 0.25

total_capital = debt_balance + equity_value
weight_d = debt_balance / total_capital
weight_e = equity_value / total_capital

wacc = (weight_e * cost_of_equity) + (weight_d * cost_of_debt * (1 - tax_rate))

print(f"--- COST OF CAPITAL (HURDLE RATE) ---")
print(f"Capital Mix: {weight_d:.1%} Debt | {weight_e:.1%} Equity")
print(f"Current WACC: {wacc:.2%}")
print("-" * 30)
print(f"ADVISORY RULE: Any new project (ROI) must yield > {wacc:.2%}.")
print(f"If a project yields 10%, REJECT IT. It is destroying value relative to your capital costs.")