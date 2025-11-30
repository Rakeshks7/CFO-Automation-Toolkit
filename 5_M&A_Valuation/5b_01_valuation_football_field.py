import matplotlib.pyplot as plt
import numpy as np

ranges = {
    '52-Week High/Low': [18.00, 25.00],
    'Comparable Companies (EV/EBITDA)': [22.00, 28.00],
    'Precedent Transactions': [24.00, 32.00], 
    'DCF (Perpetuity Method)': [20.00, 35.00], 
    'DCF (Exit Multiple)': [23.00, 30.00]
}

labels = list(ranges.keys())
mins = [v[0] for v in ranges.values()]
maxs = [v[1] for v in ranges.values()]
diffs = [m - n for m, n in zip(maxs, mins)]

plt.figure(figsize=(10, 6))

plt.barh(labels, diffs, left=mins, height=0.5, color='#34495e', alpha=0.9)

for i, (min_val, max_val) in enumerate(zip(mins, maxs)):
    plt.text(min_val - 2, i, f"${min_val:.0f}", va='center', fontsize=10)
    plt.text(max_val + 0.5, i, f"${max_val:.0f}", va='center', fontsize=10)

avg_val = np.mean(mins + maxs)
plt.axvline(avg_val, color='#e74c3c', linestyle='--', linewidth=2, label=f'Mean Valuation (${avg_val:.0f})')

plt.title("Valuation Summary ('Football Field')")
plt.xlabel("Implied Share Price ($)")
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.savefig("Valuation_Football_Field.png")
print(f"Mean Valuation Calculated: ${avg_val:.2f}")
plt.show()