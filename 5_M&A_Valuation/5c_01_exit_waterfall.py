import pandas as pd

exit_valuation = 40000000  
transaction_fees = 1500000 
debt_payoff = 2000000      

investors = [
    {'Name': 'Series A VC', 'Invested': 5000000, 'Pref_Multiple': 1.0, 'Participation': False, 'Ownership': 0.20},
    {'Name': 'Series B VC', 'Invested': 10000000, 'Pref_Multiple': 2.0, 'Participation': False, 'Ownership': 0.15},
    {'Name': 'Angel Group', 'Invested': 500000, 'Pref_Multiple': 1.0, 'Participation': False, 'Ownership': 0.05}
]

founders_ownership = 0.60 

def calculate_waterfall(val, fees, debt, investors, founder_pct):
    net_cash = val - fees - debt
    
    distribution_log = []
    
    remaining_cash = net_cash
    pref_payouts = {}
    
    for inv in investors:
        pref_amount = inv['Invested'] * inv['Pref_Multiple']
        conversion_value = net_cash * inv['Ownership']
        
        if pref_amount > conversion_value:
            payout = pref_amount
            pref_payouts[inv['Name']] = payout
            remaining_cash -= payout
            distribution_log.append(f"{inv['Name']} takes Preference: ${payout:,.0f}")
            inv['Is_Converted'] = False 
        else:
            pref_payouts[inv['Name']] = 0 
            inv['Is_Converted'] = True
    
    converted_ownership_total = founder_pct + sum(i['Ownership'] for i in investors if i['Is_Converted'])
    
    common_payouts = {}
    
    founder_share = (founder_pct / converted_ownership_total) * remaining_cash
    common_payouts['Founders'] = max(0, founder_share)
    
    for inv in investors:
        if inv['Is_Converted']:
            share = (inv['Ownership'] / converted_ownership_total) * remaining_cash
            common_payouts[inv['Name']] = share
        else:
            common_payouts[inv['Name']] = pref_payouts[inv['Name']] 

    return net_cash, common_payouts

net_cash, payouts = calculate_waterfall(exit_valuation, transaction_fees, debt_payoff, investors, founders_ownership)

print(f"--- EXIT WATERFALL ANALYSIS ---")
print(f"Gross Sale Price: ${exit_valuation:,.0f}")
print(f"Net Distributable: ${net_cash:,.0f} (After Debt/Fees)")
print("-" * 40)
print("PAYOUT TABLE:")
for stakeholder, amount in payouts.items():
    print(f"{stakeholder}: ${amount:,.0f}")

founder_take_home = payouts['Founders']
print("-" * 40)
print(f"FOUNDER RESULT: ${founder_take_home:,.0f}")
print(f"Note: Even though Founders own {founders_ownership:.0%} of the company, they received {founder_take_home/net_cash:.1%} of the cash due to Investor Preferences.")