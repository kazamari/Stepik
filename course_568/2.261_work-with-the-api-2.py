'''
In this problem, you need to use the API of the numbersapi.com website.

You are given a set of numbers. For each of the numbers you need to find out whether there is an interesting mathematical
fact about this number.

Output string Interesting for each of the numbers that have an interesting fact, and Boring otherwise.
Output the information on numbers’ interestingness in the same order, in which these numbers are presented in the input
file.

An example of request to an interesting number:
http://numbersapi.com/31/math?json=true

An example of request to a boring number:
http://numbersapi.com/999/math?json=true

Input file example:
    31
    999
    1024
    502

Output file example:
    Interesting
    Boring
    Interesting
    Boring
'''