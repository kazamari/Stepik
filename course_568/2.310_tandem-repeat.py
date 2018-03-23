'''
Given a sequence of lines.
Output the lines, which contain the word, consisting of two identical parts (tandem repeat).

Sample Input:
    blabla is a tandem repetition
    123123 is good too
    go go
    aaa

Sample Output:
    blabla is a tandem repetition
    123123 is good too
'''

import re, sys

pattern = r'\b(\S+)\1\b'

for line in sys.stdin:
    if re.search(pattern, line.rstrip()):
        print(line.rstrip())
