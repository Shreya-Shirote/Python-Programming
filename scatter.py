import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)
plt.scatter(x,y,c=colors, s=sizes)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter plot')
plt.show()
