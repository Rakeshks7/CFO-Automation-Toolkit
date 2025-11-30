import pandas as pd

data = {
    'Total_Assets': 1000000,
    'Total_Liabilities': 400000,
    'Working_Capital': 200000,  
    'Retained_Earnings': 150000,
    'EBIT': 120000,
    'Market_Value_Equity': 800000, 
    'Sales': 1500000
}

X1 = data['Working_Capital'] / data['Total_Assets']
X2 = data['Retained_Earnings'] / data['Total_Assets']
X3 = data['EBIT'] / data['Total_Assets']
X4 = data['Market_Value_Equity'] / data['Total_Liabilities']
X5 = data['Sales'] / data['Total_Assets']

Z_score = (0.717 * X1) + (0.847 * X2) + (3.107 * X3) + (0.420 * X4) + (0.998 * X5)

print(f"--- CREDIT STRENGTH DIAGNOSTIC (Z-Score) ---")
print(f"Calculated Score: {Z_score:.2f}")

print("\n--- BANKER'S INTERPRETATION ---")
if Z_score > 2.9:
    print("✅ SAFE ZONE: The bank views you as low risk. Negotiate for lower interest rates.")
elif Z_score > 1.23:
    print("⚠️ GREY ZONE: You are investable, but they will ask for personal guarantees or collateral.")
else:
    print("🚨 DISTRESS ZONE: High probability of bankruptcy/default. Loan will be rejected.")
    print("Action Plan: Increase Retained Earnings (Profit) or inject Equity to boost X2 and X4.")