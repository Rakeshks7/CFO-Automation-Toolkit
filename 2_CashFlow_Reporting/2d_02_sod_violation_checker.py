import pandas as pd

audit_log = {
    'Transaction_ID': ['T1', 'T1', 'T2', 'T2', 'T3', 'T3'],
    'Action': ['Create Vendor', 'Approve Payment', 'Create Vendor', 'Approve Payment', 'Create Vendor', 'Approve Payment'],
    'User': ['Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Alice'], 
    'Timestamp': ['2025-11-01', '2025-11-02', '2025-11-03', '2025-11-03', '2025-11-04', '2025-11-04']
}
df = pd.DataFrame(audit_log)

toxic_combos = [
    ('Create Vendor', 'Approve Payment'),
    ('Edit Bank Details', 'Approve Payment'),
    ('Create Journal Entry', 'Post Journal Entry')
]

violations = []

grouped = df.groupby('Transaction_ID')

for tx_id, group in grouped:
    users = group['User'].unique()
    
    for user in users:
        user_actions = group[group['User'] == user]['Action'].tolist()
        
        for (action_a, action_b) in toxic_combos:
            if action_a in user_actions and action_b in user_actions:
                violations.append({
                    'Transaction_ID': tx_id,
                    'User': user,
                    'Violation': f"{action_a} + {action_b}"
                })

print("--- SEPARATION OF DUTIES (SoD) REPORT ---")
if violations:
    df_v = pd.DataFrame(violations)
    print(df_v.to_string(index=False))
    print("\nACTION: Revoke approval access for these users immediately.")
else:
    print("✅ No SoD violations found.")