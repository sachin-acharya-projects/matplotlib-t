from matplotlib import pyplot as plt, animation
from random import randint
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('dev-data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

ax1.plot(ages, dev_salaries, color="#444444", linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title("Median Salary Distribution")
ax1.set_xlabel('Age')
ax1.set_ylabel('Salary')

ax2.legend()
ax2.set_xlabel('Age')
ax2.set_ylabel('Salary')

plt.tight_layout()
plt.show()