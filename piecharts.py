from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [60, 20, 30]
labels = ['JavaScript', 'Python', 'Flutter']
plt.pie(slices, labels=labels)

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()