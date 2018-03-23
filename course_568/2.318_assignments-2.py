'''
You can place multiple assignments in the single line:
    string = "14 15 16"
    a, b, c = string.split(" ")

It could be useful to determine such assignments in the code automatically, and during this to highlight all variables
within the assignment!

But yes. We forgot. The code may contain comments (!), inside which assignment does not ocur, and it would be good to
ignore assignments inside comments.

Please remember that a comment begins with the # character and continues until the end of the line like in the following
example:

    a, b, c = string.split(" ") # multiple assignment
    # a, b, c = string.split(" ") multiple assignment

We are interested only in the first string.

Still we forgot that assignments might be for object attributes. Therefore, a variable can contain points, but may not
begin with a point and may not contain two points in a row.

Python code is given on input; there may be only one assignment per line, but with several variables. It is necessary to
find all uncommented assignments and for each such assignment output a space separated line number and name of each
variable (in the same order they are in the assignment).

NB. In this problem it may be necessary to use re.match, instead of re.findall; the re.match function checks whether the
string fits the pattern (and does not find all occurrences of the pattern in the string, as re.findall does), the
re.match function returns MatchObject if the string (or the beginning of the string) fits the pattern, or None if it
doesn't. MatchObject has the groups() method, which contains grouped symbols, example of the re.match usage:

    import re
    pattern = "(ID: (\d+))"
    str1 = "ID: 5853"
    str2 = "xID: 455"
    match1 = re.match(pattern, str1)
    match2 = re.match(pattern, str2)
    print(match1)
    print(match1.groups())
    print(match2)

And, of course, a link to the documentation:﻿ https://docs.python.org/3.4/library/re.html#re.regex.match

Sample Input 1:
    #This is sample code challenge
    import random

    def generate():
        num_tests = 10
        tests = []
        for test in range(num_tests):
            a = random.randrange(10)
            b = random.randrange(10)
            test_case = "{} {}".format(a, b)
            tests.append(test_case)
        return tests

    def solve(dataset):
        a, b = dataset.split()
        return str(int(a)+int(b))

    def check(reply, clue):
        return int(reply) == int(clue)

Sample Output 1:
    5 num_tests
    6 tests
    8 a
    9 b
    10 test_case
    15 a b

Sample Input 2:
    #! /usr/bin/env python3
    #from fractions import gcd

    def euclid(a, b):
        while b:
            a, b = b, a % b
        return a
    # def euclid(n, m):
    #     x = gcd(20, 8)
    #     return x

    lst = input().split()
    n = int(lst[0])
    m = int(lst[1])
    print(euclid(n, m))

Sample Output 2:
    6 a b
    12 lst
    13 n
    14 m

Sample Input 3:
    a, b, c = 12, 13, 15
    for x in [1, 2, 3, 4]:
        a, b = x, x + 1
        # yo = x
        # to, to = 6, 5
        c, d = x + 2, x + 3  # that's ok

Sample Output 3:
    1 a b c
    3 a b
    6 c d

Sample Input 4:
    class HTTPDigestAuth:
        """Attaches HTTP Digest Authentication to the given Request object."""
        def __init__(self, username, password):
            self.username = username
            self.password = password
            # Keep state in per-thread local storage
            self._thread_local = threading.local()

Sample Output 4:
    4 self.username
    5 self.password
    7 self._thread_local
'''

import re
from sys import stdin

pattern = r'[^\S]*(([_A-Za-z][_\.\w]*, )*([_A-Za-z][_\.\w]*)) = '

for n, s in [(i+1, line.rstrip()) for i, line in enumerate(stdin)]:
    if re.match(pattern, s):
        print(n, re.match(pattern, s).group(1).replace(',', ''))
