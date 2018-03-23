'''
Given a sequence of lines.
In each line replace all occurrences of the substring "human" to the substring "computer" and output the resulting lines.

Sample Input:
    I need to understand the human mind
    humanity

Sample Output:
    I need to understand the computer mind
    computerity
'''
# Posted from PyCharm Edu
# put your python code here
import sys
print(sys.stdin.read().replace('human', 'computer'))

