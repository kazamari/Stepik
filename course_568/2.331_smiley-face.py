'''
You need to check whether the string is a smiley face.

If yes – output 1, otherwise – 0.

Smiley:
    Eyes is one of ":" ";"  ">:",
    nose "-" either one or none at all,
    mouth is one of "{", "}", "[", "]", "(", ")", "p" at least once. One type may be repeated as many times as you want.

All symbols go precisely in the listed order, smiley does not contain any other symbols.

Input data
    String with length up to 100 symbols, consisting of uppercase and lowercase letters of the Latin alphabet and
    various characters.

Output data
    Output 1, if the given string is a smiley. Otherwise output 0.

Sample Input 1:
    :)

Sample Output 1:
    1

Sample Input 2:
    :-(

Sample Output 2:
    1

Sample Input 3:
    :-()

Sample Output 3:
    0

Sample Input 4:
    :))))

Sample Output 4:
    1
'''
import re

pattern = r'(:|;|>:)-?(\)|\(|\{|\}|\[|\]|p)\2*$'

print(1 if re.match(pattern, input()) else 0)