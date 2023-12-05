import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Шаг 2: Загрузить данные и взять 1000 значений
df = pd.read_csv("test.csv")
df_sample = df.head(1000)

# Шаг 3: Проверить данные на пропуски
missing_values = df_sample.isnull().sum()
print("Пропуски в данных:")
print(missing_values)

# Шаг 4: Проверить на нормальность распределения и выбросы
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Ящик с усами на логарифмической шкале
sns.boxplot(x="Rooms", y="Square", data=df_sample, ax=axes[0, 0])
axes[0, 0].set_yscale('log')
axes[0, 0].set_title('Ящик с усами (логарифм Square)')

# Гистограмма Square
sns.histplot(df_sample['Square'], ax=axes[0, 1], kde=True)
axes[0, 1].set_title('Гистограмма Square')

# Ящик с усами на логарифмической шкале для LifeSquare
sns.boxplot(x="Rooms", y="LifeSquare", data=df_sample, ax=axes[1, 0])
axes[1, 0].set_yscale('log')
axes[1, 0].set_title('Ящик с усами (логарифм LifeSquare)')

# Гистограмма LifeSquare
sns.histplot(df_sample['LifeSquare'], ax=axes[1, 1], kde=True)
axes[1, 1].set_title('Гистограмма LifeSquare')

plt.tight_layout()
plt.show()

# Шаг 5: Заполнить пропуски и обработать аномальные значения (пример)
df_sample['Square'].fillna(df_sample['Square'].median(), inplace=True)
df_sample['LifeSquare'].fillna(df_sample['LifeSquare'].median(), inplace=True)

# Шаг 6: Определить количество комнат
room_counts = df_sample['Rooms'].value_counts()
print("Количество квартир по количеству комнат:")
print(room_counts)

# Шаг 7: Построить сводную таблицу
pivot_table = pd.pivot_table(df_sample, values='Id', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)
print("Сводная таблица:")
print(pivot_table)

# Шаг 8: Сохранить обработанный массив без выбросов и пропусков
df_sample.to_csv("surname.csv", index=False)
print("Обработанный массив сохранен в файл 'surname.csv'")


# Построение 3D графика
fig = px.scatter_3d(df_sample, x='Rooms', y='Square', z='LifeSquare',
                    color='DistrictId', size='Rooms', opacity=0.7,  # Используйте 'Rooms' вместо 'Price'
                    labels={'LifeSquare': 'Life Square', 'Square': 'Square'},
                    title='3D график параметров квартир')
fig.update_layout(scene=dict(xaxis_title='Количество комнат',
                             yaxis_title='Площадь',
                             zaxis_title='Жилая площадь'))

# Показать график
fig.show()