# 데이터 수집
A_length = [25.4, 26.5, 27.5, 28.4, 29.0, 29.2, 30.1, 30.5, 31.4, 31.2]
A_weight = [243, 290, 340, 363, 430, 450, 500, 394, 450, 500]
B_length = [5.4, 6.5, 7.5, 8.4, 9.0, 9.2, 9.1, 9.5, 1.4, 1.2]
B_weight = [43, 90, 40, 63, 30, 50, 50, 94, 50, 50]

# 데이터 정리
length = A_length + B_length
weight = A_weight + A_weight
data = [[length, weight] for length, weight in zip(length, weight)]
X = data

# A = 0, B = 1
Y = [0] * 10 + [1] * 10

# 모델 생성
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 학습
kn.fit(X, Y)

# 테스트
print(kn.predict([[30, 400]]), kn.predict([[7, 40]]))