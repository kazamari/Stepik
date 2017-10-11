'''
Вам дано описание наследования классов в формате JSON. Описание представляет из себя массив JSON-объектов, которые
соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое
содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.

Sample Input:
    [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
    A : 3
    B : 1
    C : 2
'''

import json

def count_children(cls):
    res = [cls]
    for d in classes:
        if cls in d['parents']:
            res.extend(count_children(d['name']))
    return list(set(res))

classes = json.loads(input())

for cls in sorted([x['name'] for x in classes]):
    print(cls, len(count_children(cls)), sep=' : ')