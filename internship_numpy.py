import math
import time
from copy import deepcopy

import numpy as np
from scipy.spatial.distance import cdist


rng = np.random.default_rng()

#1. Дан случайный массив, поменять знак у элементов, значения которых между 3 и 8

rnd_array = rng.integers(low=1, high=10, size=20) #создание рандомного массива размером 1-20 (range (1,10))
print(f'Исходный массив Task 1: {rnd_array}')
filter_condition = (rnd_array > 3) & (rnd_array < 8) #условие при которых изменяется знак
rnd_array[filter_condition] = rnd_array[filter_condition] * -1
print(f'Изменённый массив Task 1: {rnd_array}')


#2. Заменить максимальный элемент случайного массива на 0

print(f'Исходный массив Task 2: {rnd_array}')
max_element = rnd_array.max() #находим max()
rnd_array = np.where(rnd_array == max_element, 0, rnd_array) #в массиве где max_element замена на 0
print(f'Изменённый массив Task 2: {rnd_array}')


#3 Построить прямое произведение массивов (все комбинации с каждым элементом). На вход подается двумерный массив

rnd_array = np.arange(10).reshape(2,5) #создание двумерного массива 2х5
print(f'Исходный массив Task 3: {rnd_array}')
cross_multiply = np.kron(rnd_array[0], rnd_array[1]) #каждый элемент матрицы перемножается
cross_multiply = np.reshape(cross_multiply, (5, 5)) #форматирование массива в матрицу 5х5
print(f'Изменённый массив Task 3: {cross_multiply}')


# 4. Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B,
# независимо от порядка элементов в B

# array_a = rng.integers(low=1, high=10, size=(8, 3))
# array_b = rng.integers(low=1, high=10, size=(2, 2))
# print(array_a, array_b, sep='\n+')
#???????????????????????????????????????????????????


#5. Дана 10x3 матрица, найти строки из неравных значений (например строка [2,2,3] остается, строка [3,3,3] удаляется)

matrix = np.array([ [1, 2, 3],
                    [2, 2, 2],
                    [1, 2, 1],
                    [1, 1, 2],
                    [3, 3, 3],
                    [4, 1, 2],
                    [4, 2, 2],
                    [8, 6, 6],
                    [6, 6, 6],
                    [9, 9, 9] ])
filter_mask_1 = (matrix[:, 0] == matrix[:, 1]) & (matrix[:, 0] == matrix[:, 2]) #маска сравнивает 1ый со 2ым и 1ый с 3им
result = matrix[~filter_mask_1] #применяет маску к матрице и оставляет НЕ(~) подходящие маске строки.
print(f'Task 5: {result}')


#6. Дан двумерный массив. Удалить те строки, которые повторяются

matrix = np.array([ [1, 2, 3],
                    [2, 2, 2],
                    [1, 2, 1],
                    [2, 2, 2],
                    [4, 3, 3],
                    [4, 1, 2],
                    [4, 22, 2],
                    [8, 6, 6],
                    [4, 22, 2],
                    [2, 1, 9] ])
unique_row = np.unique(matrix, axis=0)
print(f'Task 6: {unique_row}')

#7.1 Задача 1: Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы.
# без Numpy
array = [[8, 0, 2, 2],
         [1, 0, 2, 5],
         [3, 0, 100, 6],
         [3, 4, 4, -1],
         [1, 4, 6, 5]]
multiply = 1
new_array = deepcopy(array[0:len(array[0])])
for i, j in enumerate(new_array):
    if j[i] != 0:
        multiply *= j[i]
    else: continue
print(f'Task 7.1(Python): {multiply}')

# Numpy
array = np.array([[8, 0, 2, 2],
                  [1, 0, 2, 5],
                  [3, 0, 100, 6],
                  [3, 4, 4, -1],
                  [1, 4, 6, 5]])
main_diag = array.diagonal() #определяем элементы по главной диагонали
result_multiply = np.prod(main_diag[main_diag != 0])
print(f'Task 7.1(Numpy): {result_multiply}')


#7.2 Задача 2: Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество.

# без Numpy
x = [2, 4, 1, 5, 3, 2, 1, 5]
y = [2, 5, 5, 2, 1, 3, 4, 1]
if x.sort() == y.sort(): print(f'Task 7.2(Python): {True}')
else: print(f'Task 7.2(Python): {False}')

# Numpy
x = np.array([2, 4, 1, 5, 3, 2, 1, 5])
y = np.array([2, 5, 5, 2, 1, 3, 4, 1])
multi_result = np.array_equal(x, y)
print(f'Task 7.2(Numpy): {multi_result}')


#7.3 Задача 3: Найти максимальный элемент в векторе x среди элементов, перед которыми стоит ноль.
# Например, для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.
x = [6, 2, 0, 3, 0, 0, 5, 7, 0, 9, 0, 2, 1, 0, 4]

#Python
arr = [x[i+1] for i in range(len(x)) if x[i] == 0]
print(f'Task 7.3(Python): {max(arr)}')

#Numpy
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0, 9, 0, 2, 1, 0, 4])
zero_mask = x[:-1] == 0
all_after_zero = x[1:][zero_mask]
print(f'Task 7.3(Numpy): {np.max(all_after_zero)}')


#7.4 Задача 4: Реализовать кодирование длин серий (Run-length encoding). Для некоторого вектора x необходимо вернуть кортеж
# из двух векторов одинаковой длины. Первый содержит числа, а второй - сколько раз их нужно повторить.

#Python
x = [2, 2, 2, 3, 3, 3, 5, 5, 7, 8, 8]
without_duplicates = tuple(set(x))
count_elem = [x.count(i) for i in without_duplicates]
print(f'Task 7.4(Python): {list(without_duplicates), list(count_elem)}')

#Numpy
x = np.array([2, 2, 2, 3, 3, 3, 5, 5, 7, 8, 8])
values, counts = np.unique(x, return_counts=True)
print(f'Task 7.4(Numpy): {values, counts}')


#7.5 Задача 5: Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами.
# Сравните с функцией scipy.spatial.distance.cdist по скорости работы.

#Python
A = [[1, 2, 3, 4],[5, 6, 7, 9]]
B = [0.5, 0.1, 0.3, 0.6]


def distance_metrik(point_A:list, point_B:list)->tuple:
    evkld_result = [pow((i-j), 2) for i, j in zip(point_A, point_B)]
    evklid_distance = (sum(evkld_result))**0.5
    return(evklid_distance)


start_time = time.time()
first_distance = distance_metrik(A[0], B)
second_distance = distance_metrik(A[1], B)
end_time = time.time()
print(f'Task 7.5(Python): {first_distance, second_distance}, time: {end_time - start_time}')

#Scipy
As = np.array([[1, 2, 3, 4],[5, 6, 7, 9]])
Bs= np.array([[0.5, 0.1, 0.3, 0.6]])
start_time = time.time()
distance_scipy = cdist(As, Bs)
end_time = time.time()
print(f'Task 7.5(Scipy): {distance_scipy}, time: {end_time - start_time}',end='\n')

#Numpy
An = np.array([[1, 2, 3, 4],[5, 6, 7, 9]])
Bn = np.array([0.5, 0.1, 0.3, 0.6])
start_time = time.time()
dif_result = An - Bn
pow_result = np.pow(dif_result, 2)
sum_result = np.sum(pow_result, axis=1)
distance_numpy = sum_result ** 0.5
end_time = time.time()
print(f'Task 7.5(Numpy): {distance_numpy}, time: {end_time - start_time}')


# 8.1 Просмотрите файл cereal.csv. Этот файл содержит количества калорий для различных марок хлопьев.
# Загрузите данные из файла и сохраните их как calorie_stats.

calorie_stats = np.loadtxt("./data_files/cereal.csv", delimiter=",")
# print(calorie_stats)


#8.2В одной порции CrunchieMunchies содержится 60 калорий. Насколько выше среднее количество калорий у ваших конкурентов?
# Сохраните ответ в переменной average_calories и распечатайте переменную в терминале

crunchie_calories = 60
competitor_calories = np.average(calorie_stats)
comparison_calories = competitor_calories - crunchie_calories
print(f'Task 8.2: У конкурентов, в среднем, кол-во калорий на {comparison_calories} единиц больше, '
      f'чем у "CrunchieMunchies"')


#8.3Корректно ли среднее количество калорий отражает распределение набора данных? Давайте отсортируем данные и посмотрим.

calorie_stats_sorted = np.sort(calorie_stats)
print(f'Task 8.3: {calorie_stats_sorted}')


#8.4 Вычислите медиану набора данных и сохраните свой ответ в median_calories.
# Выведите медиану, чтобы вы могли видеть, как она сравнивается со средним значением.

median_calories = np.median(calorie_stats_sorted)
print(f'Task 8.4: {median_calories}')


#8.5 Рассчитайте различные процентили и распечатайте их, пока не найдете наименьший процентиль, превышающий 60 калорий.
# Сохраните это значение в переменной nth_percentile.

def percentile(percent:int|float)->int:
    return np.percentile(calorie_stats, percent)
print(percentile(10), percentile(30), percentile(20), percentile(5), percentile(3), percentile(3.5))
nth_percentile = percentile(3.5)
print(f'Task 8.5: {nth_percentile}')


#8.6 Вместо этого давайте подсчитаем процент хлопьев, в которых содержится более 60 калорий на порцию.
# Сохраните свой ответ в переменной more_calories и распечатайте его

more_calories = calorie_stats[calorie_stats > 60].size / calorie_stats.size * 100
print(f'Task 8.6: {more_calories}')


#8.7 Рассчитайте величину отклонения, найдя стандартное отклонение,
# Сохраните свой ответ в calorie_std и распечатайте на терминале. Как мы можем включить эту ценность в наш анализ?

calorie_std = np.std(calorie_stats)
print(f'Task 8.7: {calorie_std}')


#8.8 Напишите короткий абзац, в котором кратко изложите свои выводы и то, как, по вашему мнению,
# эти данные могут быть использованы в интересах Mycrunch при маркетинге CrunchieMunchies.

print('Task 8.8: Я бы сказал что данные которые мы получили показывают хорошую возможность для развития '
      'CrunchieMunchies. Небольшое кол-во калорий в сравнении с конкурентами говорит о том что в еде мало жиров и '
      'сахара. Это является основой в здоровой и сбалансированной пище, как для взрослых так и для детей.')