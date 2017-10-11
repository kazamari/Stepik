'''
Напишите программу, вычисляющую следующее состояние поля для Game of life.

Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного конца
(поле представляет собой тор).

Формат ввода:
На первой строке указаны два целых числа через пробел -- высота и ширина поля.
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.

Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.

Sample Input 1:
    5 5
    .....
    ..X..
    ...X.
    .XXX.
    .....

Sample Output 1:
    .....
    .....
    .X.X.
    ..XX.
    ..X..

Sample Input 2:
    5 5
    .....
    .....
    .XXX.
    .....
    .....

Sample Output 2:
    .....
    ..X..
    ..X..
    ..X..
    .....

Sample Input 3:
    5 6
    ...XX.
    .XX...
    ..X...
    XX....
    X..XX.

Sample Output 3:
    .X..XX
    .XX...
    X.X...
    XXXX.X
    XXXXX.
'''


def life_step(matrix):
    n, m = len(matrix), len(matrix[0])
    def is_alive(i, j):
        neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0):
                    neighbours += bool(matrix[(i + x) % n][(j + y) % m] == 'X')
        return (matrix[i][j] == '.' and neighbours == 3) or (matrix[i][j] == 'X' and neighbours in [2, 3])

    return [['X' if is_alive(i, j) else '.' for j in range(m)] for i in range(n)]


n, m = list(map(int, input().split()))
matrix = [list(input()) for i in range(n)]

for r in life_step(matrix):
    print(''.join(r))