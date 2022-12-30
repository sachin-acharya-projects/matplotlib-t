from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.animation as animation

data = pd.read_csv("dataset.csv")

# y = data['number'][:50]
# print(y)
x = []
y = []
count = 0
# for a in range(1, 51):
#     x.append(a)

def drawGraph(i):
    global count
    count += 1
    x.append(count)
    y.append(data['number'][count])
    
    plt.cla()
    # plt.clf()
    icount = len(x) - 5
    plt.scatter(x[icount:len(x)], y[icount:len(y)])
    plt.plot(x, y)

anime = animation.FuncAnimation(plt.gcf(), drawGraph,interval=100)

plt.tight_layout(w_pad=10.0)
plt.show()

# plt.scatter(x, y)
# plt.plot(x, y)
# plt.show()