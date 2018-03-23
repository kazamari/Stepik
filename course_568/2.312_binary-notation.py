'''
Given a sequence of lines.

Output the lines, containing the binary notation of a number, divisible by 3.

Binary notation of a number is its notation in the binary numbering system.

Note: This problem can be easily solved by reduction of the string to an integer and verification of the remainder of
division by three, but still, we ask you to solve it without using reduction to a number. Try regular expressions.

Sample Input:
    0
    10010
    00101
    01001
    Not a number
    1 1
    0 0

Sample Output:
    0
    10010
    01001
'''
import sys, re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'^(1(01*0)*1|0)*$', line):
        print(line)