'''
Выведите таблицу размером n×n, заполненную целыми числами от 1 до n2 по спирали, выходящей из левого верхнего угла
и закрученной по часовой стрелке, как показано в примере.

Формат ввода:
Одна строка, содержащая одно целое число n, n>0.

Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.

Sample Input:
    5

Sample Output:
    1 2 3 4 5
    16 17 18 19 6
    15 24 25 20 7
    14 23 22 21 8
    13 12 11 10 9
'''

n, i, start = int(input()), 0, 1
matrix = [[0 for i in range(n)] for j in range(n)]

while n >= 1:
    for j in range(i, n):
        matrix[i][j] = start
        start += 1
    for j in range(i + 1, n):
        matrix[j][n-1] = start
        start += 1
    for j in range(n-2, i-1 , -1):
        matrix[n-1][j] = start
        start += 1
    for j in range(n-2, i, -1):
        matrix[j][i] = start
        start += 1
    n -= 1
    i += 1

for x in matrix:
    print(' '.join(str(y) for y in x))