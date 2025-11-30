import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'Tx_ID': [f'TX-{i}' for i in range(1000)],
    'Amount': np.random.exponential(scale=2000, size=1000).round(2), 
    'Description': ['Vendor Payment'] * 1000
}
df = pd.DataFrame(data)

materiality_threshold = 10000
sample_size_random = 20

key_items = df[df['Amount'] >= materiality_threshold].copy()
key_items['Reason'] = 'Key Item (> Threshold)'

remaining_pop = df[df['Amount'] < materiality_threshold]
random_sample = remaining_pop.sample(n=sample_size_random, random_state=42).copy()
random_sample['Reason'] = 'Random Sample'

final_sample = pd.concat([key_items, random_sample])

print(f"--- AUDIT SAMPLE PREPARATION ---")
print(f"Total Population: {len(df)} items (${df['Amount'].sum():,.0f})")
print(f"Materiality Threshold: ${materiality_threshold:,.0f}")
print("-" * 40)
print(f"1. High Value Items (Must Check): {len(key_items)}")
print(f"2. Random Sample Items:           {len(random_sample)}")
print(f"Total Sample Size:                {len(final_sample)}")
print("-" * 40)

print("SAMPLE PREVIEW:")
print(final_sample[['Tx_ID', 'Amount', 'Reason']].head().to_string(index=False))

final_sample.to_csv("Audit_Sample_Ready.csv", index=False)
print("\nAction: Locate receipts for these specific items NOW.")