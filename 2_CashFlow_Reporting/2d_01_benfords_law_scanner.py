import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
real_data = np.random.lognormal(mean=3, sigma=1, size=500) 
fake_data = np.random.randint(800, 999, size=100) 
combined_amounts = np.concatenate([real_data, fake_data])

df = pd.DataFrame({'Amount': combined_amounts})

def get_leading_digit(x):
    s = str(abs(x))
    for char in s:
        if char in '123456789':
            return int(char)
    return None

df['Leading_Digit'] = df['Amount'].apply(get_leading_digit)
actual_counts = df['Leading_Digit'].value_counts(normalize=True).sort_index()

benford_probs = {
    1: 0.301, 2: 0.176, 3: 0.125, 4: 0.097, 
    5: 0.079, 6: 0.067, 7: 0.058, 8: 0.051, 9: 0.046
}
expected = pd.Series(benford_probs)

comparison = pd.DataFrame({'Actual': actual_counts, 'Expected': expected})
comparison['Deviation'] = np.abs(comparison['Actual'] - comparison['Expected'])

print("--- BENFORD'S LAW FRAUD DETECTION ---")
print(comparison.round(3))

suspicious_digits = comparison[comparison['Deviation'] > 0.05]
if not suspicious_digits.empty:
    print("\n⚠️ ALERT: Suspicious patterns detected!")
    print("The following leading digits appear way more/less than natural probability:")
    print(suspicious_digits.index.tolist())
    print("Investigation Idea: If '9' is high, look for invoices just under approval limits (e.g., $990).")

comparison[['Actual', 'Expected']].plot(kind='bar', figsize=(10, 6))
plt.title("Benford's Law Analysis (Actual vs Theoretical)")
plt.ylabel("Frequency")
plt.xlabel("Leading Digit")
plt.savefig("Benfords_Analysis.png")
plt.show()