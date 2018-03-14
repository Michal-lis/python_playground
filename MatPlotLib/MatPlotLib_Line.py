import matplotlib.pyplot as plt
import math
from math import log10 as log

# EVERYTHING IN MATLPLOTLIB IS CUSTOMIZABLE

x = [x for x in range(2, 10, 2)]
y = [4, 6, 7, 9]
plt.bar(x, y, label='price')
plt.xlabel('Plot number')
plt.ylabel('y')
plt.title('Lipa')
plt.legend()
plt.show()
