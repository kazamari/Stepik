'''
Given a sequence of lines.
Output the lines, which contain the backslash "\".

Sample Input:
    \w denotes word character
    No slashes here

Sample Output:
    \w denotes word character
'''
from sys import stdin

[print(line.rstrip()) for line in stdin if '\\' in line]