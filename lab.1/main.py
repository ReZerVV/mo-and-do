# F=3*X1+3*X2  →  max
# X1-4*X2 <= 4
# 3*X1+2*X2 <= 6
# -X1+X2 <= 1
# X1+2*X2 >= 2
# X1,X2 >=0

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

x1 = np.linspace(0, 10, 10)
x2_1 = (4 - x1) / 4
x2_2 = (6 - 3*x1) / 2
x2_3 = 1 + x1
x2_4 = (2 - x1) / 2
F = (3-3*x1) / 3

plt.xlabel("X1")
plt.ylabel("X2")
plt.plot(x1, x2_1, label="x1-4*x2<=4")
plt.plot(x1, x2_2, label="3*x1+2*x2<=6")
plt.plot(x1, x2_3, label="-x1+x2<=1")
plt.plot(x1, x2_4, label="x1+2*x2<=2")
plt.plot(x1, F, "g--", label="Func")
plt.grid()
plt.legend()
plt.show()

c = np.array([-3, -3])
a_ub = np.array([[-1, 4], [3, 2], [1, -1], [-1, -2]])
b_ub = np.array([4, 6, 1, -2])
result = sc.linprog(c, a_ub, b_ub)
print(result)