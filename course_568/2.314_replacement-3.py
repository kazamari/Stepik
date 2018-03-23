'''
Given a sequence of lines.
In each line replace the first occurrence of the word, consisting of only the Latin letters "a" (case insensitive),
to the word "argh".

Note:
Pay attention to the count parameter of the sub function.

Sample Input:
    There’ll be no more "Aaaaaaaaaaaaaaa"
    AaAaAaA AaAaAaA

Sample Output:
    There’ll be no more "argh"
    argh AaAaAaA
'''
from sys import stdin
from re import sub

for line in stdin:
    print(sub(r'\b[Aa]+\b', r'argh', line.rstrip(), count=1))