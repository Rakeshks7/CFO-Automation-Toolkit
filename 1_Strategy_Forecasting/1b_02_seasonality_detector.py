import pandas as pd
import matplotlib.pyplot as plt

history_data = {
    'Month_Num': [1,2,3,4,5,6,7,8,9,10,11,12] * 3, 
    'Revenue': [
        10, 11, 12, 11, 12, 13, 12, 13, 14, 15, 25, 30,  
        12, 13, 13, 14, 14, 15, 15, 16, 17, 18, 28, 35,  
        15, 16, 17, 16, 17, 18, 18, 19, 20, 22, 32, 40   
    ]
}
df = pd.DataFrame(history_data)

monthly_avg = df.groupby('Month_Num')['Revenue'].mean()

overall_avg = df['Revenue'].mean()

seasonal_index = monthly_avg / overall_avg

print("--- SEASONALITY DETECTED ---")
print("Month | Seasonal Index (Weight)")
print(seasonal_index.round(2))

plt.figure(figsize=(10, 5))
seasonal_index.plot(kind='bar', color='#3498db')
plt.axhline(1.0, color='red', linestyle='--', label='Average Month')
plt.title("Seasonality Index (Proprietary Algorithm)")
plt.ylabel("Multiplier vs Average")
plt.xlabel("Month of Year")
plt.legend()
plt.show()

peak_month = seasonal_index.idxmax()
print(f"\nINSIGHT: Month {peak_month} is your peak, typically performing {seasonal_index.max():.1%} of the average month.")