from scipy.optimize import linprog

obj = [-20, -30]

lhs_ineq = [[1, 2],  
            [1, 1]]  

rhs_ineq = [100,  
            80]   

bnd = [(0, float("inf")), (0, float("inf"))]

optimization = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="highs")

if optimization.success:
    qty_std = round(optimization.x[0], 0)
    qty_deluxe = round(optimization.x[1], 0)
    max_profit = (qty_std * 20) + (qty_deluxe * 30)
    
    print("--- OPTIMIZED PRODUCTION PLAN ---")
    print(f"Produce Standard Units: {qty_std}")
    print(f"Produce Deluxe Units:   {qty_deluxe}")
    print(f"Resulting Profit:       ${max_profit:,.0f}")
    print("Insight: This mix utilizes your constraints most efficiently.")
else:
    print("Optimization failed.")