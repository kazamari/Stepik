'''
Кривая Коха -- это простой геометрический фрактал.

Строится этот фрактал следующим образом: берётся отрезок, разделяется на три равных части. Вместо средней части
вставляется два таких же отрезка, поставленные под углом 60 градусов друг к другу.

Этот процесс повторяется на каждой итерации: каждый отрезок заменяется четырьмя.

Напишите программу, которая принимает на вход число n − количество итераций генерации кривой и выводит
последовательность углов поворота при рисовании соответствующей линии от начальной точки к конечной, без отрыва пера.

Способ проверки своего решения приведён на следующем степе.

Формат ввода:
Строка с целым числом n, 1≤n≤10.

Формат вывода:
Строки, содержащие последовательность поворотов. Каждый поворот указывается на отдельной строке как слово "turn"
и угол поворота в градусах. Угол поворота должен находиться в интервале [-180; 180].

Sample Input:
    1

Sample Output:
    turn 60
    turn -120
    turn 60
'''

def Koch(n):
    if n == 0:
        return
    Koch(n - 1)
    print('turn 60')
    Koch(n - 1)
    print('turn -120')
    Koch(n - 1)
    print('turn 60')
    Koch(n - 1)


Koch(int(input()))