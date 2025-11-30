import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

risk_free_rate = 0.045      
market_risk_premium = 0.06  
tax_rate = 0.25             
unlevered_beta = 1.1        

def get_cost_of_debt(debt_ratio):
    if debt_ratio <= 0.10: return 0.060  
    elif debt_ratio <= 0.30: return 0.075
    elif debt_ratio <= 0.50: return 0.095 
    elif debt_ratio <= 0.70: return 0.130 
    else: return 0.180 

results = []
debt_levels = np.arange(0.00, 0.95, 0.05) 

for d_ratio in debt_levels:
    e_ratio = 1 - d_ratio
    if e_ratio == 0: continue
    
    de_ratio = d_ratio / e_ratio
    
    levered_beta = unlevered_beta * (1 + (1 - tax_rate) * de_ratio)
    
    cost_equity = risk_free_rate + (levered_beta * market_risk_premium)
    
    pre_tax_kd = get_cost_of_debt(d_ratio)
    after_tax_kd = pre_tax_kd * (1 - tax_rate)
    
    wacc = (cost_equity * e_ratio) + (after_tax_kd * d_ratio)
    
    results.append({
        'Debt_%': d_ratio,
        'WACC': wacc,
        'Cost_Equity': cost_equity,
        'Cost_Debt': pre_tax_kd
    })

df = pd.DataFrame(results)
optimal = df.loc[df['WACC'].idxmin()]

print("--- CAPITAL STRUCTURE STRATEGY ---")
print(f"Optimal Debt Ratio: {optimal['Debt_%']:.0%}")
print(f"Minimum WACC:       {optimal['WACC']:.2%}")
print("-" * 40)
print(f"Advisory: By moving to {optimal['Debt_%']:.0%} debt, you minimize your cost of capital.")
print(f"However, going beyond {optimal['Debt_%'] + 0.10:.0%} triggers a spike in interest rates.")

plt.figure(figsize=(10, 6))
plt.plot(df['Debt_%'], df['WACC'], label='WACC (Minimize This)', linewidth=3, color='#2c3e50')
plt.plot(df['Debt_%'], df['Cost_Equity'], label='Cost of Equity', linestyle='--', color='#e74c3c')
plt.plot(df['Debt_%'], df['Cost_Debt'], label='Cost of Debt (Pre-Tax)', linestyle='--', color='#27ae60')

plt.axvline(optimal['Debt_%'], color='gold', linestyle='-', linewidth=2, label='Optimal Point')

plt.title('Optimal Capital Structure Analysis')
plt.xlabel('Debt % (Leverage)')
plt.ylabel('Cost of Capital (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("WACC_Optimization_Curve.png")
plt.show()