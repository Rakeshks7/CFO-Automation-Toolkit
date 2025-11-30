import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# INPUTS: Client's Historical Data & Goals
# ==========================================
# In a real engagement, you'd pull this from their QuickBooks/Xero export
client_name = "TechFlow Solutions"
current_revenue = 1500000  # $1.5M
target_revenue = 2500000   # $2.5M Target for next year

# Historical Growth Rates (The "Volatility Profile")
# If they are a stable business, volatility is low. Startups have high volatility.
history = [0.10, 0.12, 0.08, 0.15, 0.05, -0.02, 0.18] # last 7 years/months growth
avg_growth = np.mean(history)
std_dev = np.std(history)

# ==========================================
# THE ENGINE: Monte Carlo Simulation
# ==========================================
simulations = 5000
results = []

np.random.seed(42) # For reproducibility during client meetings

for i in range(simulations):
    # Simulate a random growth rate based on their history
    sim_growth = np.random.normal(avg_growth, std_dev)
    projected_rev = current_revenue * (1 + sim_growth)
    results.append(projected_rev)

results = np.array(results)

# ==========================================
# DECISION METRICS
# ==========================================
# 1. Probability of Success
probability_success = np.mean(results >= target_revenue)

# 2. Downside Risk (VaR - Value at Risk)
# What is the "Worst Case" (Bottom 5% outcome)?
worst_case = np.percentile(results, 5)

# 3. Upside Potential
best_case = np.percentile(results, 95)

# ==========================================
# OUTPUT: The Narrative for the Client
# ==========================================
print(f"--- STRATEGIC SIMULATION: {client_name} ---")
print(f"Goal: Grow from ${current_revenue:,.0f} to ${target_revenue:,.0f}")
print("-" * 40)
print(f"Historical Volatility: {std_dev:.1%}")
print(f"Model Probability of Hitting Target: {probability_success:.1%}")
print("-" * 40)
print(f"📉 The 'Safety Floor' (95% confidence): We will likely make at least ${worst_case:,.0f}")
print(f"📈 The 'Blue Sky' (Top 5%): We could reach ${best_case:,.0f}")

if probability_success < 0.50:
    print("\n⚠️ STRATEGIC ADVISORY: Your target is aggressive compared to historical performance.")
    print("Recommendation: We need to inject capital or launch a new product to break the historical trend.")
else:
    print("\n✅ STRATEGIC ADVISORY: This goal is realistic and organic.")

# ==========================================
# VISUALIZATION
# ==========================================
plt.figure(figsize=(10, 6))
plt.hist(results, bins=50, color='#2c3e50', alpha=0.7, edgecolor='white')
plt.axvline(target_revenue, color='#e74c3c', linestyle='--', linewidth=2, label=f'Target (${target_revenue:,.0f})')
plt.axvline(np.mean(results), color='#f1c40f', linestyle='-', linewidth=2, label='Most Likely Outcome')

plt.title(f'Probability Distribution of Next Year Revenue\n{client_name}', fontsize=14)
plt.xlabel('Projected Revenue ($)')
plt.ylabel('Frequency of Scenarios')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Save chart for the slide deck
plt.savefig('Strategy_MonteCarlo_Chart.png')
print("\nChart saved as 'Strategy_MonteCarlo_Chart.png'")
plt.show()