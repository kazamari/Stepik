'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa﻿
'''

def countex(s, t):
    n = 0
    if t in s:
        for i in range(len(s)):
            if s[i:].startswith(t):
                n += 1
    return n

s, t = input(), input()
print(countex(s, t))