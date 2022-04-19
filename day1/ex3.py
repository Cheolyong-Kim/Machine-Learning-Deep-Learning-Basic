import numpy as np
from numpy.linalg import inv

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
in_A = inv(A)

print(in_A)

# 2x-y=0
# x+y=3

# Y=WX
# W=XY^-1
X = np.array([[2, -1], [1, 1]])
Y = np.array([[0], [3]])
in_X = inv(X)
W = in_X.dot(Y)
print(W)