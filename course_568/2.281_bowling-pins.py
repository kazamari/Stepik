'''
 N bowling pins were put in one row and numbered from left to right with numbers from 1 to N. Then K balls were thrown
 at this row; i-th ball knocked down all pins with numbers from li to ri  inclusive. Find which pins remained standing.

Input data format
On input the program gets the number of pins N and the number of throws K. Next go K pairs of numbers li, ri, with
1 ≤ li, ri ≤ N.

Output data format
The program should output the sequence of N characters, where j-th symbol is “I”, if j-th pin remained standing, or “.”,
if j-th pin was knocked down.

Sample Input:
    10 3
    8 10
    2 5
    3 6

Sample Output:
    I.....I...
'''

n, k = map(int, input().split())

pins = ['I'] * n

for i in range(k):
    l, r = map(int, input().split())
    pins[l - 1:r] = '.' * (r - l + 1)

print(''.join(pins))



