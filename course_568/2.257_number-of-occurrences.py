'''
Given two strings s and t, consisting of lowercase letters of the Latin alphabet.

Find the number of occurrences of the line t in the line s.

Example:
    s = "abababa"
    t = "aba"

There are 3 occurrences of the line t in the line s:
    abababa
    abababa
    abababa

Sample Input 1:
    abababa
    aba

Sample Output 1:
    3

Sample Input 2:
    abababa
    abc

Sample Output 2:
    0

Sample Input 3:
    abc
    abc

Sample Output 3:
    1

Sample Input 4:
    aaaaa
    a

Sample Output 4:
    5
'''


def num_occur(t, s):
    i, n = s.find(t, 0), 0
    while i >= 0:
        n += 1
        i = s.find(t, i+1)
    return n


s = input()
print(num_occur(input(), s))