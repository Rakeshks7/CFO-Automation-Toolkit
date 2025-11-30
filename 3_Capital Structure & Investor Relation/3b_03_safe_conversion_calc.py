import pandas as pd

series_a_price = 2.50  
series_a_val = 20000000 

safes = [
    {'Investor': 'Angel 1', 'Invested': 100000, 'Cap': 10000000, 'Discount': 0.20}, 
    {'Investor': 'Angel 2', 'Invested': 50000,  'Cap': 15000000, 'Discount': 0.20}, 
    {'Investor': 'Angel 3', 'Invested': 25000,  'Cap': 25000000, 'Discount': 0.10}  
]

results = []

for safe in safes:
    price_discount = series_a_price * (1 - safe['Discount'])
    
    price_cap = series_a_price * (safe['Cap'] / series_a_val)
    
    final_price = min(price_discount, price_cap)
    
    shares = safe['Invested'] / final_price
    
    results.append({
        'Investor': safe['Investor'],
        'Invested': safe['Invested'],
        'Series_A_Price': series_a_price,
        'Effective_Price': final_price,
        'Shares_Received': shares,
        'Method_Used': 'Cap' if final_price == price_cap else 'Discount'
    })

df = pd.DataFrame(results)

print("--- SAFE CONVERSION REPORT ---")
print(df[['Investor', 'Invested', 'Effective_Price', 'Method_Used', 'Shares_Received']].round(2))

bad_deal = df[df['Effective_Price'] >= series_a_price * 0.9] 
if not bad_deal.empty:
    print("\nINSIGHT: Angel 3's Cap was so high ($25M) that they barely got a deal compared to Series A.")