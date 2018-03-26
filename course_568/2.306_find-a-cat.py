'''
Given a sequence of lines.
Output all the lines, which contain "cat" as a word.

Note:
Use the groups of symbols \b и \B to work with words.                                 

You can find the description of these groups in the documentation.

Sample Input:
    cat
    catapult and cat
    catcat
    concat
    Cat
    "cat"
    !cat?

Sample Output:
    cat
    catapult and cat
    "cat"
    !cat?
'''
import re, sys
data = sys.stdin.read().splitlines()

[print(x) for x in data if re.search(r'\bcat\b', x)]