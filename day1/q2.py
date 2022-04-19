import numpy as np
from numpy.linalg import inv

# 2x+3y=1
# x-2y=4

A = np.array([[2, 3], [1, -2]])
Y = np.array([[1], [4]])
inv_A = inv(A)
X = inv_A.dot(Y)
print(X)
