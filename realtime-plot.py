from matplotlib import animation, pyplot as plt
from itertools import count
import random, pandas as pd

# Setting Styles
plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    plt.cla()
    plt.scatter(x_vals, y_vals)
    plt.plot(x_vals, y_vals)
anime = animation.FuncAnimation(plt.gcf(), animate, interval=400)

plt.tight_layout()
plt.show()