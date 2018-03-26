'''
You need to write a program that "flips" a sequence of positive integers. On input there is a sequence of space
separated positive integers. The sequence ends with zero. You are required to output the sequence in the reverse order.

The numbers should be space separated on the output. The terminating zero is simply the indicator of the end of the
sequence, it is not a part of it, i.e. you should not output it.

Sample Input:
    15 26 1 42 0

Sample Output:
    42 1 26 15
'''

print(*list(reversed(input().split()))[1:])