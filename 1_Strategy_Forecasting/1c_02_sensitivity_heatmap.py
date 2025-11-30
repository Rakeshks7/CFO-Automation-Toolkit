import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def simple_dcf(g, w):
    fcf = 1000000
    return fcf * (1+g) / (w - g) 

growth_rates = [0.02, 0.03, 0.04, 0.05, 0.06] 
discount_rates = [0.08, 0.09, 0.10, 0.11, 0.12] 

matrix_data = []

for w in discount_rates:
    row = []
    for g in growth_rates:
        if w <= g: 
            val = 0 
        else:
            val = simple_dcf(g, w) / 1000000 
        row.append(val)
    matrix_data.append(row)

df_sensitivity = pd.DataFrame(matrix_data, 
                              index=[f"WACC {x:.0%}" for x in discount_rates],
                              columns=[f"Growth {x:.0%}" for x in growth_rates])

plt.figure(figsize=(8, 6))
sns.heatmap(df_sensitivity, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5)
plt.title("Valuation Sensitivity (Enterprise Value in $M)")
plt.xlabel("Long Term Growth Rate")
plt.ylabel("Discount Rate (Risk)")

output_file = "Valuation_Heatmap.png"
plt.savefig(output_file)
print(f"Heatmap saved as {output_file}")
plt.show()