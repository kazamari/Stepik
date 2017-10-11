'''
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a operator b,
где вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения,
вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a operator b, 0 ≤ a, b ≤ 1000. Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число − результат вычисления.

Sample Input 1:
    45 plus 8

Sample Output 1:
    53

Sample Input 2:
    12 minus 42

Sample Output 2:
    -30

Sample Input 3:
    451 multiply 2

Sample Output 3:
    902

Sample Input 4:
    13 divide 3

Sample Output 4:
    4
'''

# put your python code here
m = {'plus':'+', 'minus':'-', 'multiply':'*', 'divide':'//'}
ex = input().split()
print(eval(ex[0] + m[ex[1]] + ex[2]))

# operators = {
#     'plus': lambda x, y: x + y,
#     'minus': lambda x, y: x - y,
#     'multiply': lambda x, y: x * y,
#     'divide': lambda x, y: x // y
# }
# s = input().split(' ')
# print(operators[s[1]](int(s[0]), int(s[2])))