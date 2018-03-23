'''
In this problem, we will deal with the implementation of a group of symbols.

We use wildcards "( )" to group symbols.

Grouping of characters allows us using repetitions for the sequences: thus, under the pattern "(ab)+" will fit any
string like "ababababab...ab".

Also, grouping of characters allows us to find interesting substrings inside a large pattern: for example, if we know
that somewhere inside the string is a substring "ID: 254", using the pattern "ID: (\d+)" (\d indicates any number) we
will be able to find only the number 254 we are interested in:

    import re
    string = "ID: 254, ID: 14, ID: 88"
    ids = re.findall("ID: (\d+)", string)
    print(ids)

It is important to understand that the findall function from the re module, returns tuple from all groups, which it
found, and if these groups are not listed explicitly, it considers the entire pattern as one group. If we change the
pattern to "(ID: (\d+))", the function will return tuples with two elements: the whole pattern and its digital ID.

    import re
    string = "ID: 254, ID: 14, ID: 88"
    ids = re.findall("(ID: (\d+))", string)
    print(ids)

NB. It is important to understand that the groups will be listed inside the tuple in the order of their occurrence in
the pattern. (In the order, in which occur the opening brackets, corresponding to the groups)

In this problem Python code is served as input. Your task is to find all the assignments in the code and to output
where they occurred, and the value of what variable they changed!

Please remember that according to the PEP8 standard, the operation of assignment (in contrast to the transfer of an
argument) is separated by a single space from both sides. Thus, as a valid assignment we consider if (something,
consisting of only letters, numbers and lowerspace) = (something). In this problem we believe that there may be only
one assignment of only one variable per line.

For each assignment you need to output on a separate line – the line number (lines are numbered from one) and the name
of the variable, value of which has been changed. The line numbers must be in ascending order.

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

    def combinations(n, k):
        if 0 <= k <= n:
            ncomb = 1
            kcomb = 1
            for i in range(1, min(k, n - k) + 1):
                ncomb *= n
                kcomb *= t
                n -= 1
            return ncomb // kcomb
        else:
            return 0

    lst = input().split()
    n = int(lst[0])
    k = int(lst[1])
    print(combinations(n, k))

Sample Output 1:
    5 num_tests
    6 tests
    8 a
    9 b
    10 test_case
    16 ncomb
    17 kcomb
    26 lst
    27 n
    28 k

Sample Input 2:
    str1 = input()
    lst = []
    numbers = str1.split(" ")
    for i in numbers:
        lst.append(int(i))
    mean_value = sum(lst)/(len(lst))
    print(mean_value)

Sample Output 2:
    1 str1
    2 lst
    3 numbers
    6 mean_value

Sample Input 3:
    s = input()
    s = s.lower()
    d = dict()
    l = []
    for i in s:
        l.append(i)
        d[i] = 0
    for i in l:
        for key in d:
            if key == i:
                d[i] += 1
    keys = d.keys()
    keys = list(keys)
    keys.sort()
    for i in keys:
        print(i + ' ' + str(d[i]))

Sample Output 3:
    1 s
    2 s
    3 d
    4 l
    12 keys
    13 keys
'''
import re, sys

pattern = r'\.*([_A-Za-z][_\w]*)(, )* = '

for i, line in enumerate(sys.stdin):
    if re.findall(pattern, line.rstrip()):
        [print(i+1, x[0]) for x in re.findall(pattern, line.rstrip())]