import matplotlib.pyplot as plt

data = [
    ('PY EBITDA', 500),
    ('Price Increases', 120),  
    ('Volume Growth', 80),     
    ('Cost Inflation', -90),   
    ('New Hires', -150),       
    ('FX Impact', -30),        
    ('CY EBITDA', 430)         
]

names = [x[0] for x in data]
values = [x[1] for x in data]

starts = [0]
running_sum = values[0]
colors = ['blue'] 

for i in range(1, len(values) - 1):
    change = values[i]
    if change >= 0:
        starts.append(running_sum)
        colors.append('green')
    else:
        starts.append(running_sum + change) 
        colors.append('red')
    running_sum += change

starts.append(0) 
colors.append('blue')

plot_heights = [abs(v) for v in values]
plot_bottoms = []

current = 0
for i, val in enumerate(values):
    if i == 0 or i == len(values)-1:
        plot_bottoms.append(0)
        current = val
    else:
        if val >= 0:
            plot_bottoms.append(current)
            current += val
        else:
            current += val
            plot_bottoms.append(current)

plt.figure(figsize=(12, 6))
bars = plt.bar(names, plot_heights, bottom=plot_bottoms, color=colors)

for rect, val in zip(bars, values):
    h = rect.get_height()
    b = rect.get_y()
    plt.text(rect.get_x() + rect.get_width()/2., b + h + 5, f"{val:+}", ha='center', va='bottom', fontweight='bold')

plt.title("EBITDA Bridge: Year-Over-Year Walk")
plt.ylabel("$ Thousands")
plt.axhline(0, color='black', linewidth=1)
plt.savefig("EBITDA_Bridge.png")
plt.show()