import numpy as np
"""x = np.array([[1, 2], [3, 4], [5, 6]])
z = x.reshape(6)
print(z)"""

"""x = np.arange(1, 8, 3)
print(x)
z = x.reshape(3, 1)
print(z[1][0])"""

"""x = np.arange(1,10)
print(x[x<4])
print(x[(x > 5) & (x%2 == 0)])"""

x = np.arange(1, 5)
print(x)
x = x*2
print(x[:3].sum())