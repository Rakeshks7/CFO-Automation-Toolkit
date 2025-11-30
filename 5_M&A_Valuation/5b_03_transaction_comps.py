import pandas as pd

public_ebitda_multiple = 8.5  
control_premium_low = 0.20    
control_premium_high = 0.35   
client_ebitda = 4500000

tx_multiple_low = public_ebitda_multiple * (1 + control_premium_low)
tx_multiple_high = public_ebitda_multiple * (1 + control_premium_high)

val_low = client_ebitda * tx_multiple_low
val_high = client_ebitda * tx_multiple_high

print(f"--- PRECEDENT TRANSACTION ANALYSIS ---")
print(f"Public Trading Multiple: {public_ebitda_multiple}x")
print(f"Control Premium Range:   {control_premium_low:.0%} - {control_premium_high:.0%}")
print("-" * 40)
print(f"Implied M&A Multiple:    {tx_multiple_low:.1f}x - {tx_multiple_high:.1f}x")
print(f"Implied Exit Value:      ${val_low:,.0f} - ${val_high:,.0f}")