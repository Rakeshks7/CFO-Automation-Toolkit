net_profit_before_tax = 500000
jurisdiction_tax_rate = 0.21 
state_tax_rate = 0.06

permanent_differences = 20000 
depreciation_book = 50000
depreciation_tax = 80000      

taxable_income = net_profit_before_tax + permanent_differences + (depreciation_book - depreciation_tax)

federal_tax = taxable_income * jurisdiction_tax_rate
state_tax = taxable_income * state_tax_rate
total_tax_liability = federal_tax + state_tax

effective_rate = total_tax_liability / net_profit_before_tax

print(f"--- YEAR-END TAX ESTIMATOR ---")
print(f"Book Profit:    ${net_profit_before_tax:,.0f}")
print(f"Taxable Income: ${taxable_income:,.0f} (After adjustments)")
print("-" * 30)
print(f"Estimated Tax Bill: ${total_tax_liability:,.0f}")
print(f"Effective Tax Rate: {effective_rate:.1%}")
print("-" * 30)
print(f"ADVISORY: You need to set aside ${total_tax_liability/12:,.0f} per month into a separate Tax Savings Account.")