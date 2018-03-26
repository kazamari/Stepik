'''
A positive integer number is called prime, if it has exactly two different dividers, i.e. it can be divided only by one
and by itself.
For example, number 2 is prime, as it is divided only by 1 and by 2. Other examples of prime numbers include 3, 5, 31,
and infinitely many numbers.
Number 4, as example, is not prime, because it has three dividers – 1, 2, 4. Number 1 is not prime either, as it has
only one divider – 1.

Implement the generator function primes, which will generate prime numbers in ascending order, starting from number 2.

Example use:
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
'''

def primes():
    D, q = {}, 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1