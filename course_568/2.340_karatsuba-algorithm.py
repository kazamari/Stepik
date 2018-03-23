'''
Given two long integers 1≤x,y≤1050000 in decimal, output their product xy.

Please note that some programming languages (like Haskell, Python, Java) provide long arithmetic out of the box.
Please do not use built-in functions, but implement your own procedure.

Sample Input:
    239030239030566179
    56617956617923930

Sample Output:
    13533403703804583268316967452763470
'''


def karatsuba(x, y):
    if x.bit_length() <= 64 or y.bit_length() <= 64:  # Base case
        return x * y

    m = max(x.bit_length(), y.bit_length())
    m2 = (m + 32) // 64 * 32
    mask = (1 << m2) - 1

    high1, low1 = x >> m2, x & mask
    high2, low2 = y >> m2, y & mask

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return (((z2 << m2) + z1 - z2 - z0) << m2) + z0


print(karatsuba(int(input()), int(input())))
