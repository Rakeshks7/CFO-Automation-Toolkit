import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

categories = ['Accounting Knowledge', 'Excel/Modeling', 'Communication', 'Software/Tools', 'Leadership']
current_scores = [4, 2, 3, 5, 1] 
target_scores =  [4, 4, 4, 5, 3] 

def create_radar(cats, curr, targ):
    angles = np.linspace(0, 2 * np.pi, len(cats), endpoint=False).tolist()
    
    curr += curr[:1]
    targ += targ[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, targ, color='green', linewidth=1, linestyle='--', label='Target Role')
    ax.fill(angles, targ, color='green', alpha=0.1)
    
    ax.plot(angles, curr, color='blue', linewidth=2, label='Current Level')
    ax.fill(angles, curr, color='blue', alpha=0.25)
    
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(cats)
    
    plt.title('Skills Gap Analysis: Alice', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    
    plt.savefig("Skills_Radar_Chart.png")
    plt.show()

create_radar(categories, current_scores, target_scores)

print("--- DEVELOPMENT PLAN ---")
for cat, c, t in zip(categories, current_scores, target_scores):
    gap = t - c
    if gap > 0:
        print(f"⚠️ GAP in {cat}: You are at {c}, Target is {t}. (Improve by {gap} points)")
        if cat == 'Excel/Modeling':
            print("   Action: Complete 'Advanced Financial Modeling' course by Q3.")
        elif cat == 'Leadership':
            print("   Action: Lead the intern onboarding process next month.")