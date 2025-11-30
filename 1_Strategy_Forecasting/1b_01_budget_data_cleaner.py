import pandas as pd
import numpy as np

data = {
    'Account': ['Revenue', 'Product A', 'Product B', 'Total Revenue', '', 'Expenses', 'Rent', 'Salaries', 'Total Expenses'],
    'Jan-24': [None, 10000, 15000, 25000, None, None, 2000, 5000, 7000],
    'Feb-24': [None, 11000, 14000, 25000, None, None, 2000, 5000, 7000],
    'Mar-24': [None, 12000, 16000, 28000, None, None, 2000, 5500, 7500]
}
df_raw = pd.DataFrame(data)

print("--- RAW DATA (MESSY) ---")
print(df_raw)

def clean_accounting_data(df):
    df_clean = df.dropna(subset=['Account']).copy()
    df_clean = df_clean[~df_clean['Account'].str.contains("Total", case=False, na=False)]
    
    df_clean = df_clean.fillna(0)
    
    def categorize(account_name):
        account_name = account_name.lower()
        if 'product' in account_name: return 'Revenue'
        if 'rent' in account_name or 'salary' in account_name: return 'OpEx'
        return 'Other'
        
    df_clean['Master_Category'] = df_clean['Account'].apply(categorize)
    
    return df_clean

df_cleaned = clean_accounting_data(df_raw)

print("\n--- CLEAN DATA (READY FOR FORECAST) ---")
print(df_cleaned)

df_cleaned.to_csv("budget_clean_data.csv", index=False)