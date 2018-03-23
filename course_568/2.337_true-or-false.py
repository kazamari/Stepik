'''
A user enters two float numbers. Let's assume these are A and B.

Print whether the following is true: A × B > A / B.

It is guaranteed that the second number (B) isn't zero.
Your program should simply print "True" or "False".

Sample Input:
    4.03
    1.0

Sample Output:
    False
'''
# Posted from PyCharm Edu
# put your python code here
a, b = float(input()), float(input())
print(a*b > a/b)