
import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = np.array([30, 45, 25, 50])
values2 = np.array([20, 35, 40, 30])

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values1, label='Data Set 1', color='blue', alpha=0.7)
plt.bar(categories, values2, label='Data Set 2', color='orange', alpha=0.7, bottom=values1)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart - Comparison of Data Sets')
plt.legend()
plt.show()

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(categories, values1, marker='o', label='Data Set 1', color='blue')
plt.plot(categories, values2, marker='s', label='Data Set 2', color='orange')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Graph - Comparison of Data Sets')
plt.legend()
plt.grid(True)
plt.show()
