'''
We have the following symbol mappings:

    A ↔ 00
    C ↔ 01
    G ↔ 10
    T ↔ 11

Given a string of 0's and 1's, decode the message via the above mapping and print out the resulting decoded message to
standard output.

Sample Input:
    00011011

Sample Output:
    ACGT
'''
dict = {'00':'A', '01':'C', '10':'G', '11':'T'}
s = input()
print(''.join([dict[s[i:i+2]] for i in range(0, len(s), 2)]))