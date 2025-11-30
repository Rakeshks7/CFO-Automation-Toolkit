import pandas as pd
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
budget = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100] 
actuals = [110, 115, 112, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan] 

df = pd.DataFrame({'Month': months, 'Budget': budget, 'Actual': actuals})

known_months = df.dropna()
burn_ratio = known_months['Actual'].sum() / known_months['Budget'].sum()

print(f"Current Spending vs Budget: {burn_ratio:.1%}")

def get_forecast(row):
    if pd.notna(row['Actual']):
        return row['Actual']
    else:
        return row['Budget'] * burn_ratio

df['Rolling_Forecast'] = df.apply(get_forecast, axis=1)

original_total = df['Budget'].sum()
new_forecast_total = df['Rolling_Forecast'].sum()
variance = new_forecast_total - original_total

print("\n--- FORECAST SUMMARY ---")
print(df)
print("-" * 30)
print(f"Original Annual Budget: ${original_total:,.0f}")
print(f"Projected Annual Spend: ${new_forecast_total:,.0f}")
print(f"Projected Overspend:    ${variance:,.0f}")

if variance > 0:
    print("⚠️ ADVISORY: If you don't cut costs, you will miss the year-end target.")