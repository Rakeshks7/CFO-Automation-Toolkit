import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

portfolio_value = 2000000  
confidence_level = 0.95    
time_horizon = 1           

np.random.seed(42)
returns = np.random.normal(0.0005, 0.015, 1000)

var_percent = np.percentile(returns, (1 - confidence_level) * 100)
var_dollar = portfolio_value * abs(var_percent)

cvar_percent = returns[returns <= var_percent].mean()
cvar_dollar = portfolio_value * abs(cvar_percent)

print(f"--- TREASURY RISK ASSESSMENT ($2M Portfolio) ---")
print(f"Daily Volatility: {np.std(returns):.1%}")
print("-" * 40)
print(f"1. Value at Risk (95%): ${var_dollar:,.0f}")
print(f"   (Meaning: In 95 out of 100 days, you won't lose more than ${var_dollar:,.0f})")
print(f"\n2. Expected Shortfall (CVaR): ${cvar_dollar:,.0f}")
print(f"   (Meaning: If a crash happens, expect to lose ${cvar_dollar:,.0f})")

plt.figure(figsize=(10, 6))
plt.hist(returns, bins=50, alpha=0.6, color='#e74c3c', density=True)
plt.axvline(var_percent, color='black', linestyle='--', label=f'VaR cutoff')
plt.title(f'Portfolio Risk Distribution (VaR 95%)')
plt.xlabel('Daily Return')
plt.legend()
plt.savefig("VaR_Chart.png")
plt.show()