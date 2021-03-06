'''
Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются
в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Формат ввода:
Одна строка с целыми числами, разделёнными пробелом.

Формат вывода:
Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.

Sample Input:
    4 8 0 3 4 2 0 3

Sample Output:
    0 3 4
'''

s = input().split()
print(' '.join(set([x for x in s if s.count(x) > 1])))