metrics = {
    'Month': 'November 2025',
    'Revenue': 250000,
    'MoM_Growth': 0.08,
    'Cash_Balance': 1200000,
    'Burn_Rate': 85000,
}

highlights = [
    "Closed deal with Enterprise Client X ($50k ARR)",
    "Launched new mobile app v2.0",
    "Hired VP of Sales"
]
lowlights = [
    "Churn increased slightly to 2.5%",
    "Server costs spiked due to traffic (fixing this next month)"
]
the_ask = "Intro to anyone at Acme Corp? We are trying to get a meeting."

runway = metrics['Cash_Balance'] / metrics['Burn_Rate']

email_template = f"""
Subject: {metrics['Month']} Investor Update - Growth {metrics['MoM_Growth']:.1%}

Hi Everyone,

Here is our update for {metrics['Month']}.

🚀 KEY METRICS
- Revenue: ${metrics['Revenue']:,.0f} (+{metrics['MoM_Growth']:.1%} MoM)
- Cash on Hand: ${metrics['Cash_Balance']:,.0f}
- Monthly Burn: ${metrics['Burn_Rate']:,.0f}
- Runway: {runway:.1f} Months

🌟 HIGHLIGHTS
{chr(10).join(['- ' + h for h in highlights])}

⚠️ LOWLIGHTS / CHALLENGES
{chr(10).join(['- ' + l for l in lowlights])}

🙏 THE ASK
- {the_ask}

Thank you for your support.

Best,
The Founders
"""

print("--- COPY/PASTE INTO GMAIL ---")
print(email_template)