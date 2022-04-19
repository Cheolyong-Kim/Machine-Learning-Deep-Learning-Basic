import numpy as np

a = np.array([2, 1])  # 벡터

print(np.linalg.norm(a))

m1 = np.array([[1, 2], [3, 4]])  # 행렬

m2 = np.array([[1, 2], [3, 4]])

print(m1 + m2)
print(m1 * m2)  # 행렬 곱 X, 스칼라 곱

print(np.dot(m1, m2))  # 행렬 곱, 벡터 내적

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.dot(x, y))

m_x = np.array([[1, 2, 3]])
m_y = np.array([[4, 5, 6]])

# print(np.dot(m_x, m_y))  # 행, 열이 맞지 않아서 계산이 안됨

m_y = m_y.T  # m_y의 전치 행렬
print(m_y)

print(np.dot(m_x, m_y))
print(m_x.dot(m_y))  # 위와 동일한 연산

