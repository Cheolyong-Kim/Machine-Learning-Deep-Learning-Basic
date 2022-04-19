import numpy as np

a1 = np.array([[1, 2, 3], [-1, -2, -3]])
a2 = np.array([[4, -4], [5, -5], [6, -6]])
y = np.dot(a1, a2)
print(y)