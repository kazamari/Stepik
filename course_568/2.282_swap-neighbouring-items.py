'''
Swap the position of neighbouring items of the list (A[0] with A[1], A[2] with A[3] etc.). If there is odd number of
elements in the list, the last element remains at its position.

Input data format
The first line of the input contains the number of elements in the array. The second line contains the elements of the array.

Sample Input:
    5
    1 2 3 4 5

Sample Output:
    2 1 4 3 5
'''

n, s = int(input()), input().split()

for i in range(1, n, 2):
    s[i-1], s[i] = s[i], s[i-1]

print(*s)
