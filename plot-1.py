from matplotlib import animation, pyplot as plt
from itertools import count
import random, pandas as pd, matplotlib

# Setting Styles
plt.style.use('fivethirtyeight')

index = count()
x_vals = []
y_vals = []

fig, ax = plt.subplots()
ax.set_title("Median Salary Distribution")
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
def update(i):
    x_val = next(index)
    y_val = random.randint(0, 100)
    x_vals.append(x_val)
    y_vals.append(y_val)
    
    tmin, tmax = ax.get_xlim()
    if x_val >= tmax:
        tmin += 20
        tmax += 20
        ax.set_xlim(tmin, tmax)
    ax.cla()
    ax.plot(x_vals, y_vals)

anime = animation.FuncAnimation(fig, update, interval=400)
plt.tight_layout()
plt.show()