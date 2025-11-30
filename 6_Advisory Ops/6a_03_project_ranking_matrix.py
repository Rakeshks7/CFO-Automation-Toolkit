import pandas as pd

projects = [
    {'Name': 'New ERP System', 'NPV': 50000, 'Payback_Months': 24, 'Strat_Fit': 9, 'Risk': 'High'},
    {'Name': 'Marketing Campaign', 'NPV': 120000, 'Payback_Months': 6, 'Strat_Fit': 7, 'Risk': 'Low'},
    {'Name': 'New Product R&D', 'NPV': 500000, 'Payback_Months': 36, 'Strat_Fit': 10, 'Risk': 'High'},
    {'Name': 'Office Renovation', 'NPV': 0, 'Payback_Months': 99, 'Strat_Fit': 3, 'Risk': 'Low'}
]

weights = {'NPV': 0.40, 'Payback': 0.30, 'Strategy': 0.30}

df = pd.DataFrame(projects)

df['Score_NPV'] = (df['NPV'] - df['NPV'].min()) / (df['NPV'].max() - df['NPV'].min()) * 100

df['Score_Payback'] = (df['Payback_Months'].max() - df['Payback_Months']) / (df['Payback_Months'].max() - df['Payback_Months'].min()) * 100

df['Score_Strat'] = df['Strat_Fit'] * 10

df['Total_Score'] = (df['Score_NPV'] * weights['NPV']) + \
                    (df['Score_Payback'] * weights['Payback']) + \
                    (df['Score_Strat'] * weights['Strategy'])

df = df.sort_values(by='Total_Score', ascending=False)

print("--- CAPITAL ALLOCATION RANKING ---")
print(df[['Name', 'NPV', 'Payback_Months', 'Strat_Fit', 'Total_Score']].round(1).to_string(index=False))

print("\n--- CFO RECOMMENDATION ---")
winner = df.iloc[0]
print(f"Fund '{winner['Name']}' first.")
print(f"Reason: It has the best balance of Financials and Strategy (Score: {winner['Total_Score']:.1f}).")