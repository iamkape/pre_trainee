from copy import deepcopy

import numpy as np


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