'''
On input your program gets the two strings s and t, consisting of lowercase Latin letters.
Output one number – the number of occurencies of the string t in the string s.

Example:
    s = "abababa"
    t = "aba"

Occurrences of string t into string s:
    aba baba
    ab aba ba
    abab aba

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
s, t = input(), input()
n, i = 0, -1

while True:
    i = s.find(t, i + 1)
    if i < 0:
        break
    n += 1

print(n)