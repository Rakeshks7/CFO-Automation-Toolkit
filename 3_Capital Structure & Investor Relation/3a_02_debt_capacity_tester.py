import pandas as pd

ebitda = 1200000          
capex = 100000            
taxes = 200000            
bank_dscr_req = 1.25      
loan_term_years = 5

cfads = ebitda - capex - taxes

max_annual_payment = cfads / bank_dscr_req

def calculate_max_principal(payment, rate, years):
    return payment * (1 - (1 + rate)**-years) / rate

rates = [0.06, 0.08, 0.10, 0.12]
scenarios = []

for r in rates:
    max_loan = calculate_max_principal(max_annual_payment, r, loan_term_years)
    scenarios.append({
        'Interest_Rate': r,
        'Max_Loan_Amount': max_loan,
        'Monthly_Payment': max_annual_payment / 12
    })

df = pd.DataFrame(scenarios)

print(f"--- DEBT CAPACITY ANALYSIS (CFADS: ${cfads:,.0f}) ---")
print(f"Constraint: Bank requires {bank_dscr_req}x DSCR")
print("-" * 40)
print(df.style.format({'Interest_Rate': '{:.1%}', 'Max_Loan_Amount': '${:,.0f}', 'Monthly_Payment': '${:,.0f}'}).to_string())

print("\n--- STRESS TEST ADVISORY ---")
safe_loan = df.iloc[2]['Max_Loan_Amount'] 
print(f"Recommendation: Do not request more than ${safe_loan:,.0f}.")
print("If you ask for more, the bank will likely reject it due to DSCR constraints.")