import pandas as pd

acquirer = {
    'Net_Income': 10000000,
    'Shares_Outstanding': 2000000,
    'Share_Price': 50.00,
    'EPS': 5.00  
}

target = {
    'Net_Income': 2000000,
    'Shares_Outstanding': 1000000,
    'Share_Price': 20.00,
    'EPS': 2.00
}

offer_price = 25.00         
cash_percent = 0.60         
interest_rate_on_debt = 0.08 
tax_rate = 0.25

def calculate_deal(acq, tgt, offer, pct_cash, rate, tax):
    total_cost = offer * tgt['Shares_Outstanding']
    
    cash_needed = total_cost * pct_cash
    stock_value_needed = total_cost * (1 - pct_cash)
    
    new_shares = stock_value_needed / acq['Share_Price']
    
    foregone_interest = (cash_needed * rate) * (1 - tax)
    
    combined_net_income = acq['Net_Income'] + tgt['Net_Income'] - foregone_interest
    combined_shares = acq['Shares_Outstanding'] + new_shares
    
    pro_forma_eps = combined_net_income / combined_shares
    
    return pro_forma_eps, combined_net_income

pf_eps, pf_ni = calculate_deal(acquirer, target, offer_price, cash_percent, interest_rate_on_debt, tax_rate)

impact = pf_eps - acquirer['EPS']
pct_impact = impact / acquirer['EPS']

print(f"--- M&A IMPACT ANALYSIS ---")
print(f"Acquirer Standalone EPS: ${acquirer['EPS']:.2f}")
print(f"Pro Forma EPS:           ${pf_eps:.2f}")
print("-" * 30)

if impact > 0:
    print(f"✅ VERDICT: ACCRETIVE by ${impact:.2f} ({pct_impact:.1%})")
    print("The deal increases shareholder value immediately.")
else:
    print(f"⚠️ VERDICT: DILUTIVE by ${impact:.2f} ({pct_impact:.1%})")
    print("The deal lowers EPS. You need significant synergies to justify this.")