
import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма случайных данных с нормальным распределением')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()


### 2. Построение диаграммы рассеяния для двух наборов случайных данных,
# сгенерированных с помощью `numpy.random.rand`

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # 100 случайных чисел для оси X
y = np.random.rand(100)  # 100 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, color='orange')
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Случайные значения X')
plt.ylabel('Случайные значения Y')
plt.grid()
plt.show()

### 3. Парсинг цен на диваны с сайта divan.ru в CSV файл, обработка данных и построение гистограммы цен

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма случайных данных с нормальным распределением')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # 100 случайных чисел для оси X
y = np.random.rand(100)  # 100 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, color='orange')
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Случайные значения X')
plt.ylabel('Случайные значения Y')
plt.grid()
plt.show()


### 3. Парсинг цен на диваны с сайта divan.ru в CSV файл, обработка данных и построение гистограммы цен


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы, которую нужно спарсить
url = 'https://divan.ru'  # Используйте реальный URL страницы с ценами на диваны

# Получение HTML-кода страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Настройка драйвера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL страницы, которую нужно спарсить
url = 'https://www.divan.ru/product/divan-numo-velvet-pink'  # Используйте реальный URL страницы с ценами на диваны

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")  # Исправлено на правильный синтаксис

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace(' ₽/мес.', '').replace(' ', '').replace('₽', ''))

# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        cleaned_row = [clean_price(row[0])]
        writer.writerow(cleaned_row)

print(f"Обработанные данные сохранены в файл {output_file}")

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'Price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()
