from sklearn.datasets import *
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

d = load_digits()

d.images[0].flatten()

t = load_boston()
df = pd.DataFrame(t.data, columns=t.feature_names)
df['가격'] = t.target
x = t.data
y = t.target

m = LinearRegression()
m.fit(x, y)

out_d = m.predict(t.data)
plt.scatter(y, out_d)
plt.show()