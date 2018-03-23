'''
A pie costs A dollars and B cents. Find how many dollars and cents you need to pay for N pies.

Input data format
    The program gets three numbers as input: A, B, N - integers, positive, don't exceed 10000.

Output data format
    The program should output two numbers separated by a space: cost of the purchase in dollars and cents.

Sample Input 1:
    10
    15
    2

Sample Output 1:
    20 30

Sample Input 2:
    2
    50
    4

Sample Output 2:
    10 0
'''
a, b, n = int(input()), int(input()), int(input())
total = a*n*100 + b*n
print(total//100, total%100)
