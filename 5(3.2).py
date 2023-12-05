import numpy as np
import matplotlib.pyplot as plt

# Создание сетки значений x и y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)

# Функции
z1 = np.power(x, 1/4) + np.power(y, 1/4)
z2 = np.power(x, 2) - np.power(y, 2)
z3 = 2*x + 3*y
z4 = x**2 + y**2
z5 = 2 + 2*x + 2*y - x**2 - y**2

# Построение графиков
plt.figure(figsize=(15, 5))

# График 1
plt.subplot(231)
plt.contourf(x, y, z1, cmap='viridis')
plt.colorbar()
plt.title('z = x^(1/4) + y^(1/4)')

# График 2
plt.subplot(232)
plt.contourf(x, y, z2, cmap='viridis')
plt.colorbar()
plt.title('z = x^2 - y^2')

# График 3
plt.subplot(233)
plt.contourf(x, y, z3, cmap='viridis')
plt.colorbar()
plt.title('z = 2x + 3y')

# График 4
plt.subplot(234)
plt.contourf(x, y, z4, cmap='viridis')
plt.colorbar()
plt.title('z = x^2 + y^2')

# График 5
plt.subplot(235)
plt.contourf(x, y, z5, cmap='viridis')
plt.colorbar()
plt.title('z = 2 + 2x + 2y - x^2 - y^2')

plt.show()
