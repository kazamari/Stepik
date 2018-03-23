'''
Given a sequence of lines.

Output the lines, containing two letters "z" between which there are exactly three characters.

Sample Input:
    zabcz
    zzz
    zzxzz
    zz
    zxz
    zzxzxxz

Sample Output:
    zabcz
    zzxzz
'''

import sys, re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'z.{3}z', line):
        print(line)