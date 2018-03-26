'''
Find the greatest common denominator of the two integers.

Sample Input:
    779820539 641724086

Sample Output:
    1
'''


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print(gcd(a, b))
