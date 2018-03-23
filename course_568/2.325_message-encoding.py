'''
We will be dealing with a trivial example of message encoding, where the mapping of original symbols to the "code" is
simply taking the ASCII value of the symbol. For example, the "code" version of the letter 'A' would be 65.

You will be given as input a string of any length consisting of any possible ASCII characters. You must print out the
numerical ASCII value of each character of the string, separated by spaces.

Sample Input:
    Hello, World!

Sample Output:
    72 101 108 108 111 44 32 87 111 114 108 100 33
'''

print(' '.join([str(ord(i)) for i in input()]))
