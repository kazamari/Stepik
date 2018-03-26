'''
A user inputs a word.
Remove all letters that are in even positions in the word, and print what's left.

Sample Input:
    Blackbeard

Sample Output:
    Baker
'''
s = input()
# print(''.join([s[x] for x in range(0, len(s), 2)]))
print(input()[::2])