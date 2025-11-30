import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

offer_prices = [20, 22, 25, 28, 30] 
synergy_levels = [0, 200000, 500000, 800000, 1000000] 

def quick_accretion_calc(price, syn):
    cost = price * 1000000 
    interest = (cost * 0.6 * 0.08) * 0.75 
    combined_ni = 10000000 + 2000000 + (syn * 0.75) - interest
    new_shares = (cost * 0.4) / 50 
    pf_eps = combined_ni / (2000000 + new_shares)
    return (pf_eps - 5.00) / 5.00 

matrix_data = []

for s in synergy_levels:
    row = []
    for p in offer_prices:
        val = quick_accretion_calc(p, s)
        row.append(val)
    matrix_data.append(row)

df = pd.DataFrame(matrix_data, 
                  columns=[f"Price ${p}" for p in offer_prices],
                  index=[f"Syn ${s/1000:.0f}k" for s in synergy_levels])

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt=".1%", cmap="RdYlGn", center=0)
plt.title("Deal Sensitivity: Accretion / (Dilution) %")
plt.xlabel("Offer Price Per Share")
plt.ylabel("Annual Synergies")
plt.savefig("Deal_Sensitivity_Heatmap.png")
print("Heatmap generated.")
plt.show()