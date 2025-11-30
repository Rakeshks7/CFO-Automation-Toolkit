import pandas as pd

tasks = {
    'Task': ['Run Payroll', 'Bank Recs', 'Tax Filing', 'Invoicing'],
    'Alice': [1, 1, 0, 1],
    'Bob':   [0, 1, 1, 0], 
    'Charlie':[0, 1, 0, 1]
}
df = pd.DataFrame(tasks)

df['Qualified_Staff'] = df.drop('Task', axis=1).sum(axis=1)

critical_risks = df[df['Qualified_Staff'] == 1]

print("--- KNOWLEDGE SILO AUDIT ---")
print(df[['Task', 'Qualified_Staff']])

if not critical_risks.empty:
    print("\n🚨 CRITICAL RISKS DETECTED (Bus Factor = 1):")
    for idx, row in critical_risks.iterrows():
        owner = row.drop(['Task', 'Qualified_Staff']).idxmax()
        print(f"  - Task: '{row['Task']}' is owned ONLY by {owner}.")
    
    print("\nAdvisory: You must cross-train a second person on these tasks immediately.")
else:
    print("\n✅ Team is resilient. All tasks have backup coverage.")