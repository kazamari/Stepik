'''
There are two horses on a chess board and four coordintes x1, y1, x2, y2 are typed in. Determine, whether they can hit
each other or not.

INPUT
Four integer coordinates in the following sequence: x1,y1,x2,y2. The coordinates are not the same.

OUTPUT
"YES" (uppercase), if they hit each other and "NO" if they don't.

Sample Input 1:
    4 4 2 5

Sample Output 1:
    YES

Sample Input 2:
    4 4 6 6

Sample Output 2:
    NO

Sample Input 3:
    4 4 6 5

Sample Output 3:
    YES
'''
x1, y1, x2, y2 = map(int, input().split())
print('YES' if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) else 'NO')
