'''
In this problem, we will look how to implement re-occurrence of a symbol using regular expressions.

We may use the three various constructions to implement the repeat:

1.   Wildcards { }, inside which we can place the minimum/maximum number of repeats that we are satisfied with, or the
exact number of repeats that we are looking for. For example, the pattern "A{3, 5}" will fit all substrings, consisting
of consecutive characters А, with length from 3 to 5, and the pattern "T{4}" will fit only those substrings, which
contain 4 T in a row.

2.   Wildcard *. This wildcard means any number of occurrences of a character (or a group of characters): from zero to
any number you want. Thus, the pattern "A*" fits all sequences, consisting of any number of consecutive А, and fits an
empty string (as zero also fits).

3.   Wildcard +. This wildcard means any positive number of occurrences of a character (or a group of characters): from
zero to any number you want. This way, the pattern "A+" fits all sequences, consisting of any number of consecutive А.
Unlike "А*", the empty string will not fit.

All repeat meta characters are applied to a character after which they occur (or group of characters).

Examples of usage:
    import re
    results = re.findall("A+", "AAATATAGCGC")
    print(results)
    results = re.findall("TA{2}", "AATATAGCGTATA")
    print(results)

Given the list of phone numbers (each line contains one phone number). Your task is to check whether these phone numbers
are "cool": a phone number is called "cool", if it contains 3 or more same digits in a row. For example, number
19992034050 is a "cool" one, but 19500237492 is not.

Your task is to leave only the cool numbers: the standard output should contain "cool" numbers, each number on a
separate line.

Sample Input:
    89273777416
    89273777167
    89273776902
    89273778915
    89273778982
    89273774216
    89273771708
    89273772982
    89273775302
    89273775244
    89273777007
    89273778140
    89273778817
    89273770487
    89273772728
    89273773272
    89273777273
    89273779341
    89273779862
    89273772225

Sample Output:
    89273777416
    89273777167
    89273777007
    89273777273
    89273772225
'''
# Posted from PyCharm Edu
import re, sys
results = [line.strip() for line in sys.stdin if re.match(r'.*(\d)\1{2}.*', line)]
print('\n'.join(results))

