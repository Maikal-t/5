import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Заданные параметры
x_value = 3.567
a_values = np.arange(-5, 12.1, 2.5)

# Функция f(x)

def f(x, a):
    return np.sin(x / 3) + 1.2 * a

# Создание массива значений функции для каждого значения a
function_values = f(x_value, a_values)

# Вывод значений аргумента и функции
for a, value in zip(a_values, function_values):
    print(f"a = {a}, f(x) = {value}")

# Нахождение наибольшего, наименьшего, среднего значения и количество элементов массива
max_value = np.max(function_values)
min_value = np.min(function_values)
mean_value = np.mean(function_values)
array_length = len(function_values)

print(f"\nМаксимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")
print(f"Среднее значение: {mean_value}")
print(f"Количество элементов массива: {array_length}")

# Сортировка массива (чётные варианты – по убыванию, нечётные – по возрастанию)
if array_length % 2 == 0:
    sorted_function_values = np.sort(function_values)[::-1]
else:
    sorted_function_values = np.sort(function_values)

# Построение графика
plt.plot(a_values, function_values, label='f(x)')
plt.axhline(y=mean_value, color='r', linestyle='--', label='Среднее значение')

# Добавление меток и легенды
plt.xlabel('Значение a')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.legend()

# Отображение графика
plt.show()
