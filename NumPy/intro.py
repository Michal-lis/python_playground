import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

a = np.array([[1, 2, 3, 4], [3, 5, 6, 8]], dtype=float)
b = np.array([3, 5, 6, 8])

c = a * b
# d = c.sum()
# c = a.dot(b)
s = np.sin(c)

print(a)
# returns the type of every variable (in numpy array every variable is the same data type)
print(a.dtype)
# returns the number of bytes for each varibale
print(a.itemsize)
# returns the size of array (the number of variables)
print(a.size)
# returns the number of rows
print(len(a))
# return the number of rows and columns
print(a.shape)
# plt.plot(s)
# plt.show()
