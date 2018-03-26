'''
Output all the given points in ascending order of their distance from the origin of the coordinate system.

Input data
The program gets the set of points in the plane as input. First goes the number of points – n, then is a sequence of n
lines, each of which contains two numbers: the coordinates of the point. The value n does not exceed 100, all of the
initial coordinates are integers, not exceeding 1000.

Sample Input:
    2
    1 2
    2 3

Sample Output:
    1 2
    2 3
'''

n = int(input())
points = [list(map(int, input().split())) for i in range(n)]

for x, y in sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2)**.5):
    print(x, y)
