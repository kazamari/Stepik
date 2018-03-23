'''
N squirrels found K nuts and decided to divide them equally. Find how many nuts will be left after each of the squirrels
takes the equal amount of nuts.

Input data format
    There are two positive integers N and K, each of them is not greater than 10000.

Sample Input:
    3
    14

Sample Output:
    2
'''
# Posted from PyCharm Edu
n, k = int(input()), int(input())
print(k % n)