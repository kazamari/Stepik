'''
Encoding of repeats is carried as the following: s = 'aaaabbсaa' is converted into 'a4b2с1a2', that is, the groups of
the same characters of the input string are replaced by the symbol and the number of its repetitions in this string.

Write a program that reads a line from the file corresponding to the string, compressed using the repetition coding, and
performs the reverse operation, obtaining the source string.

Output the obtained string into a file and attach it as a solution to this problem.

The original string does not contain any numbers; it means that the code is definitely interpretable.

Sample Input:
    a3b4c2e10b1

Sample Output:
    aaabbbbcceeeeeeeeeeb
'''