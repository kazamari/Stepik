'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''

with open('dataset_24465_4.txt', 'r') as f:
    # for line in f.readlines()[::-1]:
    #     print(line.strip())
    with open('test_24465_4.txt', 'w') as file:
        for line in f.readlines()[::-1]:
            file.write(line)