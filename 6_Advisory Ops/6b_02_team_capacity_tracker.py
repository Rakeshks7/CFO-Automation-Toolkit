import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Role': ['Jr', 'Sr', 'Jr', 'Mgr'],
    'Hours_Logged': [45, 55, 20, 40], 
    'Standard_Capacity': [40, 40, 40, 40]
}
df = pd.DataFrame(data)

df['Utilization_%'] = df['Hours_Logged'] / df['Standard_Capacity']

def assess_status(util):
    if util > 1.10: return "🔥 BURNOUT RISK"
    if util > 0.90: return "⚠️ High Load"
    if util < 0.60: return "❄️ Underutilized"
    return "✅ Healthy"

df['Status'] = df['Utilization_%'].apply(assess_status)

print("--- TEAM CAPACITY REPORT ---")
print(df[['Employee', 'Hours_Logged', 'Utilization_%', 'Status']].to_string(index=False))

print(f"\nAverage Utilization: {df['Utilization_%'].mean():.1%}")

overworked = df[df['Utilization_%'] > 1.0]
if not overworked.empty:
    print(f"\nACTION REQUIRED: {len(overworked)} employees are overworked.")
    print("Strategy: Shift tasks from Bob (55h) to Charlie (20h) immediately.")