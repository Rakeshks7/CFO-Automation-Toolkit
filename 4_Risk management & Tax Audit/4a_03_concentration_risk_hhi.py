import pandas as pd

data = {
    'Customer': ['Amazon', 'Walmart', 'Target', 'Mom&Pop_1', 'Mom&Pop_2'],
    'Revenue':  [800000,   100000,   50000,    25000,       25000] 
}
df = pd.DataFrame(data)

total_rev = df['Revenue'].sum()
df['Share'] = df['Revenue'] / total_rev
df['Share_Sq'] = df['Share'] ** 2

hhi_index = df['Share_Sq'].sum()

print(f"--- REVENUE CONCENTRATION RISK ---")
print(f"Total Revenue: ${total_rev:,.0f}")
print(f"HHI Score: {hhi_index:.2f} (Max 1.0)")

print("\n--- RISK DIAGNOSTIC ---")
if hhi_index > 0.25:
    print("🚨 CRITICAL RISK: Highly Concentrated Portfolio.")
    print(f"Your top customer ({df.iloc[0]['Customer']}) is {df.iloc[0]['Share']:.0%} of revenue.")
    print("If they leave, the business collapses.")
elif hhi_index > 0.15:
    print("⚠️ MODERATE RISK: Moderate Concentration.")
else:
    print("✅ LOW RISK: Healthy Diversification.")