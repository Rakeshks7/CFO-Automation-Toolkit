import pandas as pd
import numpy as np

vendors = [
    {'Name': 'Vendor A', 'Price': 100000, 'Terms_Days': 0,  'Quality': 8, 'Speed': 7}, 
    {'Name': 'Vendor B', 'Price': 105000, 'Terms_Days': 60, 'Quality': 9, 'Speed': 8}, 
    {'Name': 'Vendor C', 'Price': 95000,  'Terms_Days': 0,  'Quality': 5, 'Speed': 6}  
]

df = pd.DataFrame(vendors)

cost_of_capital = 0.10 
weights = {'Price': 0.50, 'Quality': 0.30, 'Speed': 0.20}

df['Effective_Cost_PV'] = df['Price'] / ((1 + cost_of_capital) ** (df['Terms_Days'] / 365))
df['Cash_Flow_Benefit'] = df['Price'] - df['Effective_Cost_PV']

min_price = df['Effective_Cost_PV'].min()
df['Score_Price'] = (min_price / df['Effective_Cost_PV']) * 100

df['Score_Quality'] = (df['Quality'] / df['Quality'].max()) * 100
df['Score_Speed'] = (df['Speed'] / df['Speed'].max()) * 100

df['Total_Score'] = (df['Score_Price'] * weights['Price']) + \
                    (df['Score_Quality'] * weights['Quality']) + \
                    (df['Score_Speed'] * weights['Speed'])

df = df.sort_values(by='Total_Score', ascending=False)

print("--- VENDOR SELECTION MATRIX ---")
print(df[['Name', 'Price', 'Terms_Days', 'Effective_Cost_PV', 'Total_Score']].round(2).to_string(index=False))

winner = df.iloc[0]
print(f"\n🏆 WINNER: {winner['Name']}")
print(f"Reason: Best mix of Price, Terms, and Quality.")
if winner['Cash_Flow_Benefit'] > 1000:
    print(f"Insight: Their payment terms save us ${winner['Cash_Flow_Benefit']:,.0f} in real economic value.")