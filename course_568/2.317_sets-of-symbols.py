'''
In this problem we will learn how to specify sets of symbols in regular expressions.

For this we will use the [ ] wild cards.

Inside the square brackets we would be able to list all the characters that we are satisfied with: we can write the
pattern "[abc]bc", which will fit the strings abc, bbc, и cbc:

    import re
    results = re.findall("[abc]bc", "abc bbc cbc abb")
    print(results)

The expression [abc] should be regarded as one symbol, which describes: either a, or b, or с.

Other way to specify a set of symbols is to use the alteration wildcard |.

Let us describe a group of characters inside the parentheses and use the alteration character: "(a|b|c)bc"
    import re
    results = re.findall("(a|b|c)bc", "abc bbc cbc abb")
    print(results)

Compared to a set of symbols, specified by the [ ] wildcards, alteration sign can be used for a non-single-character
sequences:  thus, three strings - "abcx", "abex" and "ddx" will fit for the pattern "(abc|abe|dd)x".

In this problem, you get text on input. By using regular expressions you need to find all the occurrences of the "you"
or "You" substring in it and output their quantity.

Sample Input 1:
    What are you doing here?

Sample Output 1:
    1

Sample Input 2:
    You are not you when you are hungry

Sample Output 2:
    3

Sample Input 3:
    PART I
    IT WAS A PLEASURE TO BURN
    IT was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his
    fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his
    hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the
    tatters and charcoal ruins of history. With his symbolic helmet numbered 451 on his stolid head, and his eyes all
    orange fl

Sample Output 3:
    0
'''
# Posted from PyCharm Edu
import re
import sys
results = len(re.findall("(y|Y)ou", sys.stdin.read()))
print(results)