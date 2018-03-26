'''
Given a text file that contains some number of non-empty lines.
Using this file, generate the new text file, which contains the same lines in the reversed order.

Input file example:
    ab
    c
    dde
    ff

Output file example:
    ff
    dde
    c
    ab
'''
with open('dataset_28255_1.txt', 'r') as f:
    with open('test_28255_1.txt', 'w') as file:
        for line in f.readlines()[::-1]:
            file.write(line)