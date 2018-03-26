'''
Input – one line of random text. The text contains words and integer numbers. Your program should calculate and output
the sum of all integers that appear in the text.

Sample Input 1:
    3 5 2 2 10 quick over 9 fox brown dog

Sample Output 1:
    31

Sample Input 2:
    dog 6 5 3 lazy quick The

Sample Output 2:
    14

Sample Input 3:
    The the 4 lazy 4 The 4 jumps over jumps 3

Sample Output 3:
    15
'''

# sum = 0
# for i in input().split():
#     if i.isdigit():
#         sum += int(i)
# print(sum)

print(sum([int(x) for x in input().split() if x.isdigit()]))