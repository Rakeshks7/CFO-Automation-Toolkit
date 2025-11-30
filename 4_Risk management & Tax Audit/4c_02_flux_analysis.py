import pandas as pd

data = {
    'Account': ['Cash', 'AR', 'Inventory', 'Prepaids', 'Revenue', 'Rent Expense', 'Legal Fees'],
    'CY_Balance': [500000, 120000, 80000, 10000, 2000000, 120000, 50000],
    'PY_Balance': [100000, 115000, 80000, 5000,  1500000, 120000, 5000] 
}
df = pd.DataFrame(data)

threshold_abs = 10000
threshold_pct = 0.10

df['Diff_$'] = df['CY_Balance'] - df['PY_Balance']
df['Diff_%'] = (df['Diff_$'] / df['PY_Balance']).fillna(0)

def needs_explanation(row):
    if abs(row['Diff_$']) >= threshold_abs and abs(row['Diff_%']) >= threshold_pct:
        return "YES"
    return "No"

df['Requires_Comment'] = df.apply(needs_explanation, axis=1)

to_explain = df[df['Requires_Comment'] == "YES"]

print("--- FLUCTUATION ANALYSIS (FLUX) ---")
print(f"Criteria: > ${threshold_abs} AND > {threshold_pct:.0%}")
print("-" * 40)

if not to_explain.empty:
    print(to_explain[['Account', 'CY_Balance', 'PY_Balance', 'Diff_$', 'Diff_%']].to_string(index=False))
    print("\nAction: Write a 1-sentence reason for these spikes (e.g., 'Legal Fees increased due to IP lawsuit').")
else:
    print("✅ No material fluctuations found.")