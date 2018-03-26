'''
Check whether the point belongs to the given filled area (simple parabolas – y = (x-a)^2 + b )

Sample Input:
    6.84574546928264 6.634946548013364

Sample Output:
    NO
'''

x, y = map(float, input().split())

# if (x - 3)**2 + (y + 3)**2 < 25 or (x + 3)**2 + (y + 3)**2 < 9:
#     print('YES' if y > (x + 4)**2 - 4 or y > x else 'NO')
# else:
#     print('NO')

print('YES' if ((x - 3)**2 + (y + 3)**2 < 25 and y > x) or ((x + 3)**2 + (y + 3)**2 < 9 and y > (x + 4)**2 - 4) else 'NO')