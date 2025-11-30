import matplotlib.pyplot as plt
import numpy as np

fixed_costs = 50000      
price_per_unit = 100
variable_cost_per_unit = 40

current_sales_units = 1200

contribution_margin = price_per_unit - variable_cost_per_unit
breakeven_units = fixed_costs / contribution_margin
breakeven_revenue = breakeven_units * price_per_unit

safety_margin_units = current_sales_units - breakeven_units
safety_margin_pct = safety_margin_units / current_sales_units

print("--- BREAK-EVEN ANALYSIS ---")
print(f"Break-Even Point: {breakeven_units:.0f} units (${breakeven_revenue:,.0f})")
print(f"Current Sales:    {current_sales_units:.0f} units")
print("-" * 30)
print(f"Margin of Safety: {safety_margin_pct:.1%}")

if safety_margin_pct < 0.10:
    print("⚠️ DANGER: You are operating too close to the break-even point.")
else:
    print("✅ HEALTHY: You have a buffer against a downturn.")

units = np.linspace(0, current_sales_units * 1.5, 100)
revenue = units * price_per_unit
total_costs = fixed_costs + (units * variable_cost_per_unit)

plt.figure(figsize=(10, 6))
plt.plot(units, revenue, label='Revenue', color='green')
plt.plot(units, total_costs, label='Total Costs', color='red')
plt.axvline(breakeven_units, color='black', linestyle='--', label=f'BEP ({breakeven_units:.0f} units)')

plt.fill_between(units, revenue, total_costs, where=(revenue > total_costs), color='green', alpha=0.1)
plt.fill_between(units, revenue, total_costs, where=(revenue < total_costs), color='red', alpha=0.1)

plt.title('Cost-Volume-Profit (CVP) Analysis')
plt.xlabel('Units Sold')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("Breakeven_Chart.png")
plt.show()