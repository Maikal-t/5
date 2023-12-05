import numpy as np

a = float(3.14)

n = float(input("Введите x :\n"))
y = float(np.sin(a / 6) + (np.sqrt(3 + n) ** 2) - (np.log(n - 1) ** 3))
m = float(np.arcsin(n / 2))
r = float(y / m)
print(r)
