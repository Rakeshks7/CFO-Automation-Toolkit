import pandas as pd

data = {
    'Line_Item': ['Revenue', 'COGS', 'Gross Profit', 'Marketing', 'Salaries', 'Net Income'],
    'Actual':    [150000, 60000, 90000, 25000, 40000, 25000],
    'Budget':    [140000, 50000, 90000, 15000, 40000, 35000]
}
df = pd.DataFrame(data)

df['Var_$'] = df['Actual'] - df['Budget']
df['Var_%'] = (df['Var_$'] / df['Budget']).fillna(0)

def generate_commentary(row):
    item = row['Line_Item']
    var_dlr = row['Var_$']
    var_pct = row['Var_%']
    
    val_str = f"${abs(var_dlr):,.0f}"
    pct_str = f"{abs(var_pct):.1%}"
    
    is_expense = item in ['COGS', 'Marketing', 'Salaries']
    
    if var_dlr == 0:
        return f"Steady: {item} landed exactly on budget."
    
    if is_expense:
        if var_dlr > 0:
            return f"⚠️ Negative: {item} was over budget by {val_str} ({pct_str})."
        else:
            return f"✅ Positive: {item} came in under budget by {val_str}."
    else:
        if var_dlr > 0:
            return f"✅ Positive: {item} beat budget by {val_str} ({pct_str})."
        else:
            return f"⚠️ Negative: {item} missed budget by {val_str} ({pct_str})."

df['Commentary'] = df.apply(generate_commentary, axis=1)

print("--- MONTHLY VARIANCE REPORT ---")
print(df[['Line_Item', 'Actual', 'Budget', 'Var_$', 'Commentary']].to_string(index=False))

biggest_miss = df.loc[df['Var_$'].abs().idxmax()]
print("\n--- CFO EXECUTIVE HIGHLIGHT ---")
print(f"The most significant deviation this month was {biggest_miss['Line_Item']}.")
print(biggest_miss['Commentary'])