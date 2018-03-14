import matplotlib.pyplot as plt
import math
from math import log10 as log

# EVERYTHING IN MATLPLOTLIB IS CUSTOMIZABLE

diagram_range = 4
x = range(2, diagram_range)
constant = [0] * diagram_range
# bi-logarithmic
loglog = [log(log(x1)) for x1 in x]
# logarithmic
log = [log(x1) for x1 in x]
# polylogarithmic
pol = [x1 ** 0.5 for x1 in x]
# linear
lin = x
# linear logarithmic
linlog = [x1 * math.log10(x1) for x1 in x]
# quadratic
quad = [x1 ** 2 for x1 in x]
# quadratic logarithmic
quadlog = [x1 ** 2 * math.log10(x1) for x1 in x]
# cubic
cubic = [x1 ** 3 for x1 in x]
# base-2 exponential
base2 = [2 ** x1 for x1 in x]
# natural exponential
basee = [math.exp(x1) for x1 in x]
# base-3 exponential
base3 = [3 ** x1 for x1 in x]
# factorial
factorial = [math.factorial(x1) for x1 in x]
print(factorial[-1])
# hyper-exponential
hyp_exp = [x1 ** x1 for x1 in x]

# plt.plot(x, loglog, label='Log-log')
# plt.plot(x, log, label='Logarythmic')
# plt.plot(x, pol, label='Polylogarythmic')
# # plt.plot(x, lin, label='Linear')
# plt.plot(x, linlog, label='Linear-Log')
# plt.plot(x, quad, label='Quadratic')
# plt.plot(x, quadlog, label='Quadlog')
# plt.plot(x, cubic, label='Cubic')
# plt.plot(x, base2, label='Base2')
# plt.plot(x, basee, label='Basee')
# plt.plot(x, base3, label='Base3')
plt.plot(x, factorial, label='Factorial')
plt.plot(x, hyp_exp, label='Hyper Exponential')
plt.xlabel('x')
plt.ylabel('None')
plt.title('Computational complexity')
plt.legend()
plt.show()

# x = [1, 2, 3]
# y = [4, 6, 9]
# X2 = [12, 14, 17]
# plt.plot(x, y, label='First')
# plt.plot(x, X2, label='Second')
# plt.xlabel('Plot number')
# plt.ylabel('y')
# plt.title('Lipa')
# plt.legend()
# plt.show()
