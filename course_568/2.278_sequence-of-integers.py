'''
Write a program that reads the sequence of integers, separated by spaces, and then deletes from it all of the numbers
that are placed on the even positions, and after this outputs the resulting sequence in the reverse order.

Note In this task input can be empty.

Sample Input:
    1 2 3 4 5 6 7

Sample Output:
    6 4 2
'''

try:
    s = input().split()[1::2]
    print(*s[::-1])
except(EOFError):
    pass