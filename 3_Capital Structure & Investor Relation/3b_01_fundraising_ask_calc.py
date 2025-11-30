import pandas as pd

monthly_burn = [50000, 55000, 60000, 65000, 70000, 75000, 
                80000, 85000, 90000, 95000, 100000, 105000,
                110000, 115000, 120000, 125000, 130000, 135000,
                140000, 145000, 150000, 155000, 160000, 165000]

months_to_milestone = 18 
buffer_months = 6        

required_runway = months_to_milestone + buffer_months
total_burn_needed = sum(monthly_burn[:required_runway])

one_time_costs = 150000

total_ask = total_burn_needed + one_time_costs

print(f"--- FUNDRAISING STRATEGY ---")
print(f"Goal: Reach Series A Metrics in {months_to_milestone} months.")
print(f"Safety Buffer: {buffer_months} months.")
print("-" * 30)
print(f"Total Capital Required: ${total_ask:,.0f}")
print(f"Implied Avg Monthly Burn: ${total_burn_needed/required_runway:,.0f}")
print("-" * 30)
print("ADVISORY SCRIPT:")
print(f"'We are raising ${round(total_ask/1000000, 1)}M to give us {required_runway} months of runway.'")
print("'This capital gets us to the $1M ARR milestone with a 6-month safety cushion.'")