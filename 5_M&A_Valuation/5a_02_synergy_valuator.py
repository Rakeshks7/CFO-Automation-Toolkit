import pandas as pd

synergies = [
    {'Category': 'Headcount', 'Description': 'Eliminate Duplicate CFO Role', 'Amount': 200000, 'Confidence': 1.0},
    {'Category': 'Real Estate', 'Description': 'Close Target HQ Office', 'Amount': 150000, 'Confidence': 0.9},
    {'Category': 'COGS', 'Description': 'Bulk Purchasing Discount', 'Amount': 500000, 'Confidence': 0.7},
    {'Category': 'Revenue', 'Description': 'Cross-sell Product A to Target List', 'Amount': 1000000, 'Confidence': 0.4} # Risky
]

df = pd.DataFrame(synergies)

df['Risk_Adjusted_Value'] = df['Amount'] * df['Confidence']

tax_rate = 0.25
df['After_Tax_Value'] = df['Risk_Adjusted_Value'] * (1 - tax_rate)

total_synergy_value = df['After_Tax_Value'].sum()

cap_rate = 0.10
enterprise_value_added = total_synergy_value / cap_rate

print("--- SYNERGY VALUATION ---")
print(df[['Category', 'Description', 'Amount', 'Confidence', 'Risk_Adjusted_Value']].to_string(index=False))
print("-" * 60)
print(f"Total Annual Risk-Adjusted Savings (After Tax): ${total_synergy_value:,.0f}")
print(f"Value Created (at 10x Multiple): ${enterprise_value_added:,.0f}")

print("\nAdvisory: The Revenue synergy is high risk (40%).")
print("Focus on the 'Hard Synergies' (Headcount/Rent) to justify the deal price.")