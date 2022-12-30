from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('seaborn')

data = pd.read_csv('dev-data.csv')

ages = data['Age']
salary = data['All_Devs']
python = data['Python']

plt.bar(ages, salary, color="#111111", label='All Devs', width=0.3)
plt.plot(ages, python, color="#aaaaaa", label='Python')

plt.legend()
plt.title("Median Salary (USD)")
plt.xlabel('Ages')
plt.ylabel("Salary")
plt.tight_layout()
plt.show()