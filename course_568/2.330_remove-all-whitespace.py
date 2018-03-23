'''
Jack doesn't like when Amy puts spaces before punctuation marks, but Amy cannot possibly get rid of this habit! Help
Amy construct a regular expression, which will remove all whitespace characters before punctuation marks, not to freak
out Jack.

Input data
    On the input, you get the non-empty string with length up to 100 characters, containing the lowercase and uppercase
    letters of the Latin alphabet, as well as various signs. The string has no leading and trailing spaces. Punctuation
    marks, before which you should remove the whitespace characters (in this case: spaces and tabulations):
     . , ! ? ) ; : " ' - (you can copy them).

Output data
    The resulting string after removal of all these whitespace characters.

Sample Input 1:
    Hi !How are u   ?

Sample Output 1:
    Hi!How are u?

Sample Input 2:
    I	'm fine , thanks.

Sample Output 2:
    I'm fine, thanks.
'''
import re


def clear_text(text):
    pattern = r'\s+([.,!?);:"\'-])'
    return re.sub(pattern, r'\1', text)


print(clear_text(input()))
