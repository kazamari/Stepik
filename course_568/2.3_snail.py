'''
Snail creeps up the vertical pole of height H feets. Per day it goes A feets up, and per night it goes B feets down.
In which day the snail will reach the top of the pole?

Input data format
    On the input the program receives non-negative integers H, A, B, where H > B and A > B. Every integer does not
    exceed 100.

Sample Input:
    10
    3
    2

Sample Output:
    8
'''
# Posted from PyCharm Edu
h, a, b = [int(input()) for x in range(3)]
d = 1
while (h - a) > 0:
    h = h - a + b
    d += 1
print(d)