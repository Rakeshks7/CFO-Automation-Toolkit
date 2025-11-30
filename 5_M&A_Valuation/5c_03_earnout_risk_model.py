import numpy as np
import matplotlib.pyplot as plt

base_payment = 10000000
earnout_max = 5000000
target_revenue = 15000000  
current_revenue = 12000000

avg_growth = 0.15 
std_dev = 0.10    

iterations = 5000
results = []

for i in range(iterations):
    growth = np.random.normal(avg_growth, std_dev)
    projected_rev = current_revenue * (1 + growth)
    
    if projected_rev >= target_revenue:
        payout = earnout_max
    elif projected_rev <= current_revenue:
        payout = 0
    else:
        pct_achieved = (projected_rev - current_revenue) / (target_revenue - current_revenue)
        payout = earnout_max * pct_achieved
        
    results.append(payout)

avg_payout = np.mean(results)

print(f"--- EARNOUT RISK ASSESSMENT ---")
print(f"Max Possible Earnout: ${earnout_max:,.0f}")
print(f"Simulated Expected Value: ${avg_payout:,.0f}")
print(f"Probability of $0 Payout: {np.mean(np.array(results) == 0):.1%}")
print("-" * 40)
print(f"Advisory: Don't value this deal at ${base_payment + earnout_max:,.0f}.")
print(f"Value it at ${base_payment + avg_payout:,.0f}.")