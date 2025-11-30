import pandas as pd

current_shares = {
    'Founder A': 4000000,
    'Founder B': 4000000,
    'Early Employees': 1000000,
    'Existing Pool': 500000 
}

deal_terms = {
    'Pre_Money_Valuation': 20000000,
    'Investment_Amount': 5000000,
    'Target_Post_Money_Pool': 0.15 
}

def calculate_series_a(shares, terms):
    total_existing_shares = sum(shares.values())
    
    post_money_val = terms['Pre_Money_Valuation'] + terms['Investment_Amount']
    
    investor_pct = terms['Investment_Amount'] / post_money_val
    pool_pct = terms['Target_Post_Money_Pool']
    existing_pct = 1 - investor_pct - pool_pct
    
    total_post_shares = total_existing_shares / existing_pct
    
    pps = post_money_val / total_post_shares
    
    investor_shares = total_post_shares * investor_pct
    total_pool_shares = total_post_shares * pool_pct
    
    new_pool_shares = total_pool_shares - shares['Existing Pool']
    
    results = []
    for name, count in shares.items():
        if name == 'Existing Pool': continue
        results.append({'Stakeholder': name, 'Shares': count, 'Pct': count/total_post_shares})
        
    results.append({'Stakeholder': 'Series A Investors', 'Shares': investor_shares, 'Pct': investor_pct})
    results.append({'Stakeholder': 'Total Option Pool', 'Shares': total_pool_shares, 'Pct': pool_pct})
    
    return pd.DataFrame(results), pps, new_pool_shares

df, price, pool_increase = calculate_series_a(current_shares, deal_terms)

print(f"--- CAP TABLE POST-MONEY ---")
print(f"Share Price: ${price:.2f}")
print(f"New Options Created (Dilution): {pool_increase:,.0f} shares")
print("-" * 40)
df['Pct'] = df['Pct'].map('{:.1%}'.format)
df['Shares'] = df['Shares'].map('{:,.0f}'.format)
print(df.to_string(index=False))

founder_ownership = df.loc[df['Stakeholder'] == 'Founder A', 'Pct'].values[0]
print(f"\n⚠️ REALITY CHECK: Founder A ownership drops to {founder_ownership}.")
print("Note: The Option Pool increase came entirely out of your pre-money valuation.")