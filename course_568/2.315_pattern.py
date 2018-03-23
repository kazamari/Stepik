'''
The simplest example of a pattern is a string that contains the characters that we want to find. For example, the string
"abc" is the pattern for the string "abc", thus

    import re
    results = re.findall("abc", "abcAbcabc")
    print(results)

Outputs all occurrence of the string "abc" in the string "abcAbcabc"

In this problem, you get text as an input. By using regular expressions you need to find all occurrences of the "you"
substring in it and output their number.

NB. In this problem, you should also consider the case of letters.

NB. In this problem,you can use the following code to read the standard input:

    import sys
    data = sys.stdin.read()

as the text inside the test may consist of multiple lines, and input() reads line by line.

Sample Input 1:
    What are you doing here?

Sample Output 1:
    1

Sample Input 2:
    You are not you when you are hungry

Sample Output 2:
    2

Sample Input 3:
    PART I
    IT WAS A PLEASURE TO BURN
    IT was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his fists,
    with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were
    the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and
    charcoal ruins of history. With his symbolic helmet numbered 451 on his stolid head, and his eyes all orange fl

Sample Output 3:
    0
'''

# Posted from PyCharm Edu
import re, sys
results = re.findall(r'you', sys.stdin.read())
print(len(results))

