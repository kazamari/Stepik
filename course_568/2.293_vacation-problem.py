'''
Write a Python program to figure out what day you would return, given the day you leave and how many days you will be gone.
For example:
    If you leave on a Friday and you are gone for two (2) days, you would return on a Sunday.
    If you leave on a Monday and you are gone for eight (8) days, you would return on a Tuesday.
    If you leave on a Wednesday and you are gone 23 days, you would return on a Friday.

The program should ask for the day to leave and how many days the person will be away.

A sample conversation should look like:
    What day are you leaving? Wednesday
    How many days will you be gone? 32
    If you left on Wednesday and returned 32 days later, you would return on Sunday

One way to attack this problem is convert the days into numbers. For example, 0 = Sunday, 1 = Monday, and so on until
6 = Saturday. You might use a way to find the remainder to solve the vacation problem.

Sample Input 1:
    Friday
    19

Sample Output 1:
    If you leave on Friday and return 19 days later, you will return on Wednesday.

Sample Input 2:
    Wednesday
    64

Sample Output 2:
    If you leave on Wednesday and return 64 days later, you will return on Thursday.

Sample Input 3:
    Monday
    10

Sample Output 3:
    If you leave on Monday and return 10 days later, you will return on Thursday.
'''
weekdays = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
leave = input()
l, d = weekdays.index(leave), int(input())
r = (l + d) % 7

print("If you leave on {} and return {} days later, you will return on {}.".format(leave, d, weekdays[r]))