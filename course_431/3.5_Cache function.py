'''
Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое целочисленое
значение и возвращает его в качестве результата работы.

Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного
аргумента x.

Напишите программу, которая вычисляет значение этой функции для n чисел.

Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.

Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения
кода на тесте.

Формат ввода:
На первой строке находится число n − количество значений, на которых нужно посчитать функцию. После этого следует
n строк, на каждой строке по одному целому числу.

Формат вывода:
n строк, в каждой из которой результат вычисления функции на соответствующем аргументе.

Sample Input:
    5
    5
    12
    9
    20
    12

Sample Output:
    11
    41
    47
    61
    41
'''

from functools import lru_cache

def f(n):
    pass

f = lru_cache(maxsize=None, typed=False)(f)

for x in [int(input()) for x in range(int(input()))]:
    print(f(x))


# n, dict, list = int(input()), {}, []
#
# for x in range(n):
#     num = (int(input()))
#     list.append(num)
#     if num not in dict.keys():
#         dict[num] = f(num);
#
# for key in list:
#     print(dict[key])
