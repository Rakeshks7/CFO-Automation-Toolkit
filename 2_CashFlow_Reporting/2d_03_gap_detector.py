import pandas as pd
import numpy as np

data = {
    'Ref_Number': [1001, 1002, 1004, 1005, 1007, 1008, 1009]
}
df = pd.DataFrame(data)

min_val = df['Ref_Number'].min()
max_val = df['Ref_Number'].max()
full_range = set(range(min_val, max_val + 1))

existing_refs = set(df['Ref_Number'])
missing_refs = sorted(list(full_range - existing_refs))

print(f"--- SEQUENCE GAP ANALYSIS (Range {min_val}-{max_val}) ---")

if missing_refs:
    print(f"⚠️ MISSING TRANSACTIONS DETECTED: {len(missing_refs)}")
    print(f"Gap List: {missing_refs}")
    print("\nAdvisory Questions:")
    print("1. Were these checks voided? If so, where is the voided check?")
    print("2. Were these invoices deleted? Check the Recycle Bin/Audit Trail.")
else:
    print("✅ Sequence is intact. No missing items.")