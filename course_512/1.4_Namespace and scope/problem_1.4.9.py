'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:
    - create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    - add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    - get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
    - пространства <namespace>, или None, если такого пространства не существует

Sample Input:
    9
    add global a
    create foo global
    add foo b
    get foo a
    get foo c
    create bar foo
    add bar a
    get bar a
    get bar b

Sample Output:
    global
    None
    bar
    foo
'''
ns = {'global': {'parent':'', 'vars': []}}

def func(*args):
    def create(namespace, parent):
        if not namespace in ns.keys():
            ns.update({namespace: {'parent': parent}})

    def add(namespace, var):
        if namespace in ns.keys():
            if not 'vars' in ns[namespace].keys():
                ns[namespace].update({'vars':[var]})
            else:
                ns[namespace]['vars'].append(var)

    def get(namespace, var):
        if namespace == '':
            return None
        elif 'vars' in ns[namespace].keys() and var in ns[namespace]['vars']:
            return namespace
        else:
            return get(ns[namespace]['parent'], var)

    ff = {'create': create, 'add': add, 'get': get}
    ff[args[0]](args[1], args[2]) if args[0] != 'get' else print(ff[args[0]](args[1], args[2]))


n = int(input())
for i in range(n):
    func(*input().split())