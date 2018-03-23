'''
We have the following symbol mappings:

    A ↔ 00
    C ↔ 01
    G ↔ 10
    T ↔ 11

Given a string of A's, C's, G's, and T's, encode the message via the above mapping and print out the resulting encoded
message to standard output.

Sample Input:
    ACGT

Sample Output:
    00011011
'''

dict = {v:k for k, v in {'00':'A', '01':'C', '10':'G', '11':'T'}.items()}
s = input()
print(''.join([dict[char] for char in s]))
