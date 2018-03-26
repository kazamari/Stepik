'''
Given two integers 1≤a,b≤2⋅109.
Find the smallest integer m, which can be divided both by a, and by b.

Sample Input:
    18 35

Sample Output:
    630
'''


def lcm(a, b):
    m = a * b
    while b > 0:
        a, b = b, a % b
    return m // a


a, b = map(int, input().split())
print(lcm(a, b))
