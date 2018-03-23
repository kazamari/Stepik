'''
Some school have decided to create three new math groups and equip classrooms for them with the new desks. Only two
students may sit at any desk. The number of students in each of the three groups is known. Output the smallest amount
of desks, which will need to be purchased. Each new group sits in its own classroom.

Input data format
    The program receives the input of the three non-negative integers: the number of students in each of the three
    classes (the numbers do not exceed 1000).

Sample Input 1:
    20
    21
    22

Sample Output 1:
    32

Sample Input 2:
    16
    18
    20

Sample Output 2:
    27
'''
# Posted from PyCharm Edu
# put your python code here
classes, sum = [int(input())for i in range(3)], 0

for x in classes:
    sum += x//2 if x % 2 == 0 else x//2+1

print(sum)