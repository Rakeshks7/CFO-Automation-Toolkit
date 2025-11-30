import pandas as pd

peers = [
    {'Ticker': 'COMP1', 'Price': 50, 'Shares': 10, 'Debt': 100, 'Cash': 20, 'LTM_Rev': 200, 'LTM_EBITDA': 50},
    {'Ticker': 'COMP2', 'Price': 30, 'Shares': 20, 'Debt': 50,  'Cash': 10, 'LTM_Rev': 300, 'LTM_EBITDA': 40},
    {'Ticker': 'COMP3', 'Price': 80, 'Shares': 5,  'Debt': 200, 'Cash': 50, 'LTM_Rev': 150, 'LTM_EBITDA': 30}
]

client_financials = {'LTM_Rev': 180, 'LTM_EBITDA': 45}

df = pd.DataFrame(peers)

df['Market_Cap'] = df['Price'] * df['Shares']
df['EV'] = df['Market_Cap'] + df['Debt'] - df['Cash']

df['EV/Revenue'] = df['EV'] / df['LTM_Rev']
df['EV/EBITDA'] = df['EV'] / df['LTM_EBITDA']

median_rev_mult = df['EV/Revenue'].median()
median_ebitda_mult = df['EV/EBITDA'].median()

implied_val_rev = client_financials['LTM_Rev'] * median_rev_mult
implied_val_ebitda = client_financials['LTM_EBITDA'] * median_ebitda_mult

print("--- COMPARABLE ANALYSIS ---")
print(df[['Ticker', 'EV', 'EV/Revenue', 'EV/EBITDA']].round(2))
print("-" * 40)
print(f"Median EV/Revenue: {median_rev_mult:.2f}x")
print(f"Median EV/EBITDA:  {median_ebitda_mult:.2f}x")
print("-" * 40)
print(f"Implied Client EV (Revenue Method): ${implied_val_rev:,.0f}")
print(f"Implied Client EV (EBITDA Method):  ${implied_val_ebitda:,.0f}")