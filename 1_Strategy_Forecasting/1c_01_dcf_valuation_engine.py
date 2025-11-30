import pandas as pd
import numpy as np

current_fcf = 1000000      
growth_rate_rapid = 0.20   
growth_rate_stable = 0.03  
wacc = 0.12                
shares_outstanding = 1000000
net_debt = 500000          

def calculate_dcf(fcf, rapid_growth, terminal_growth, discount_rate, years=5):
    future_fcfs = []
    for i in range(1, years + 1):
        fcf = fcf * (1 + rapid_growth)
        future_fcfs.append(fcf)
    
    terminal_value = (future_fcfs[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
    
    pv_fcfs = sum([val / ((1 + discount_rate) ** (i+1)) for i, val in enumerate(future_fcfs)])
    pv_terminal = terminal_value / ((1 + discount_rate) ** years)
    
    enterprise_value = pv_fcfs + pv_terminal
    
    return {
        'Enterprise_Value': enterprise_value,
        'PV_Explicit_Period': pv_fcfs,
        'PV_Terminal_Value': pv_terminal,
        'Projected_FCFs': future_fcfs
    }

valuation = calculate_dcf(current_fcf, growth_rate_rapid, growth_rate_stable, wacc)

equity_value = valuation['Enterprise_Value'] - net_debt
share_price = equity_value / shares_outstanding

print("--- DCF VALUATION SUMMARY ---")
print(f"Enterprise Value: ${valuation['Enterprise_Value']:,.0f}")
print(f"  - From 5Y Operations: ${valuation['PV_Explicit_Period']:,.0f} ({(valuation['PV_Explicit_Period']/valuation['Enterprise_Value']):.1%})")
print(f"  - From Terminal Value: ${valuation['PV_Terminal_Value']:,.0f} ({(valuation['PV_Terminal_Value']/valuation['Enterprise_Value']):.1%})")
print("-" * 30)
print(f"Equity Value:     ${equity_value:,.0f}")
print(f"Implied Share Price: ${share_price:.2f}")

if valuation['PV_Terminal_Value'] / valuation['Enterprise_Value'] > 0.7:
    print("\n⚠️ NOTE: Over 70% of value is in the distant future. This valuation is highly sensitive to the Terminal Growth assumption.")