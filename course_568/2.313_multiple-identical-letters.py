'''
Given a sequence of lines.
In each line replace all occurrences of multiple identical letters by one letter.

A symbol from the group \w is considered a letter.

Sample Input:
    attraction
    buzzzz

Sample Output:
    atraction
    buz
'''
from sys import stdin
from re import sub

[print(sub(r'(\w)\1+', r'\1', line.rstrip())) for line in stdin]
