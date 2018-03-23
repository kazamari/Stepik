'''
Let's start! Solve this problem in PyCharm Edu.

Given the series of numbers: 1, -0.5, 0.25, -0.125, ... . Try to understand how it works.
On the input, the program has integer n, and the output should be a real number corresponding to the sum of first n
elements of the series.

Note:  if you have any problems with installing or logging in PyCharm Edu, please tell us about it in comments.

Sample Input:
    5

Sample Output:
    0.6875
'''
# Posted from PyCharm Edu
# write your answer here
print(sum([(-1)**i/(2**i) for i in range(int(input()))]))