'''
A user enters a phrase, which is just a bunch of words separated by commas.
Print the second word in the sentence (it is guaranteed that there's at least two words there).

Sample Input:
    nitwit, blubber, oddment, tweak

Sample Output:
    blubber
'''
print(input().split(', ', 2)[1])