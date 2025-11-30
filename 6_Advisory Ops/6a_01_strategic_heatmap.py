import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

price = 100
cost = 60
volume = 50000
fixed_costs = 1200000

base_ebitda = (price * volume) - (cost * volume) - fixed_costs

price_changes = [-0.10, -0.05, 0.00, 0.05, 0.10]
vol_changes =   [-0.20, -0.10, 0.00, 0.10, 0.20]

matrix_data = []

for v_chg in vol_changes:
    row = []
    for p_chg in price_changes:
        new_p = price * (1 + p_chg)
        new_v = volume * (1 + v_chg)
        
        new_ebitda = (new_p * new_v) - (cost * new_v) - fixed_costs
        
        row.append(round(new_ebitda / 1000, 0))
    matrix_data.append(row)

df = pd.DataFrame(matrix_data, 
                  index=[f"Vol {x:+.0%}" for x in vol_changes],
                  columns=[f"Price {x:+.0%}" for x in price_changes])

plt.figure(figsize=(10, 6))

base_k = base_ebitda / 1000
sns.heatmap(df, annot=True, fmt='g', cmap='RdYlGn', center=base_k, linewidths=.5)

plt.title(f'EBITDA Sensitivity Impact ($000s)\nBase Case: ${base_k:,.0f}k')
plt.xlabel('Pricing Strategy')
plt.ylabel('Volume Impact')
plt.savefig("Board_Strategy_Heatmap.png")
print("Strategy Map generated.")
plt.show()