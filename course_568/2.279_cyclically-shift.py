'''
Cyclically shift the elements of the list to the right (A[0] goes to the place of A[1], A[1] - to the place of
A[2], ..., and the last element goes to the place of A[0]).

Input data format
The first line of the input contains the number of elements in the array. The second line – the elements of the array.

Sample Input:
    5
    1 2 3 4 5

Sample Output:
    5 1 2 3 4
'''

n, l = int(input()), input().split()
print(*[l[(i - 1) % n] for i in range(n)])