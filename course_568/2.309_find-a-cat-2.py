'''
You have been given a sequence of lines.
Output the lines which contain "cat" as a substring at least twice.

Note:
You can read all lines from the standard input stream by the following code:
    import sys

    for line in sys.stdin:
        line = line.rstrip()
        # process line

Sample Input:
    catcat
    cat and cat
    catac
    cat
    ccaatt

Sample Output:
    catcat
    cat and cat
'''

import sys, re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'cat', line)) >= 2:
        print(line)
