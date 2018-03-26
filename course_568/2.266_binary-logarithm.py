'''
Write a program to calculate the integer-valued logarithm to base 2 (binary logarithm).

Input – first line contains an integer T, next go the T lines with tests. Each tests consists of one positive integer
ai<109. For each ai you need to output on a separate line such largest number p, that 2p≤ai. It is guaranteed that ai≥1.
While solving this problem, you can define any functions you need any. Moreover, it is recommended to put the
calculation of the logarithm into a separate function.

Sample Input:
    5
    1549
    44998
    23663
    55682
    38927

Sample Output:
    10
    15
    14
    15
    15
'''

from math import log2

l = [int(input()) for i in range(int(input()))]
for x in l:
    print(int(log2(x)))