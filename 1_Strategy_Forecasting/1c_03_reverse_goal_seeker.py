import numpy as np

current_revenue = 2000000    
target_valuation = 50000000  
years_to_exit = 5
industry_multiple = 5.0      

required_revenue = target_valuation / industry_multiple

required_cagr = (required_revenue / current_revenue) ** (1 / years_to_exit) - 1

print(f"--- PATH TO ${target_valuation/1000000:.0f}M EXIT ---")
print(f"Current Revenue:  ${current_revenue:,.0f}")
print(f"Required Revenue: ${required_revenue:,.0f} (Based on {industry_multiple}x Multiple)")
print("-" * 40)
print(f"REQUIRED ANNUAL GROWTH (CAGR): {required_cagr:.1%}")
print("-" * 40)

print("Your Roadmap:")
curr = current_revenue
for i in range(1, years_to_exit + 1):
    curr = curr * (1 + required_cagr)
    print(f"Year {i}: ${curr:,.0f}")