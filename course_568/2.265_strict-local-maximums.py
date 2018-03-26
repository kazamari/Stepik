'''
The element of a sequence is called a local maximum, if it is strictly greater than the previous and the subsequent
element of the sequence. The first and the last elements of the sequence are not the local maximum.

Given the sequence of natural numbers, ending with number 0. The number 0 itself is not included into the sequence and
serves as a sign of its end.

Find the number of strict local maximums in this sequence.

Sample Input:
    1
    2
    1
    2
    1
    0

Sample Output:
    2
'''

l, x = [], int(input())

while x != 0:
    l.append(x)
    x = int(input())

print(sum([1 for i in range(1, len(l)-1) if l[i-1] < l[i] > l[i+1]]))

