'''
Given a sequence of lines.
In each line swap the first two letters in every word, consisting of at least two letters.

A symbol from the group \w is considered a letter.

Sample Input:
    this is a text
    "this' !is. ?n1ce,

Sample Output:
    htis si a etxt
    "htis' !si. ?1nce,
'''

from sys import stdin
from re import sub

for line in stdin:
    print(sub(r'\b(\w)(\w)', r'\2\1', line.rstrip()))