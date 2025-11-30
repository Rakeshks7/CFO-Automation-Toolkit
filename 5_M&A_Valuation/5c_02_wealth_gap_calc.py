import numpy as np

current_age = 45
life_expectancy = 90
annual_spend = 200000      
inflation_rate = 0.03
investment_return = 0.05   
capital_gains_tax = 0.25   

current_savings = 500000   

years_in_retirement = life_expectancy - current_age

real_rate = (1 + investment_return) / (1 + inflation_rate) - 1
capital_needed = annual_spend * (1 - (1 + real_rate)**-years_in_retirement) / real_rate

gap = capital_needed - current_savings

required_exit_proceeds = gap / (1 - capital_gains_tax)

print(f"--- RETIREMENT FEASIBILITY CHECK ---")
print(f"Annual Burn: ${annual_spend:,.0f} (Inflation Adjusted)")
print(f"Capital Needed to Retire Today: ${capital_needed:,.0f}")
print(f"Current Liquid Savings: ${current_savings:,.0f}")
print("-" * 40)
print(f"THE GAP: ${gap:,.0f}")
print(f"REQUIRED POST-TAX EXIT PROCEEDS: ${gap:,.0f}")
print(f"REQUIRED PRE-TAX EXIT PROCEEDS:  ${required_exit_proceeds:,.0f}")
print("-" * 40)
print(f"Advisory: Do not accept an offer below ${required_exit_proceeds/1000000:.1f}M unless you plan to get another job.")