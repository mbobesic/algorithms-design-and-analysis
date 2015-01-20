__author__ = 'mislav'
from random import randint

# using as simple as possible helper methods


def add_string(a,b):
    return str(int(a)+int(b))


def subtract_string(a, b):
    return str(int(a)-int(b))


def multiply_string(a, b):
    return str(int(a)*int(b))


def karatsuba_multiplication(first, second):

    if len(first) < 10 or len(second) < 10:
        return multiply_string(first,second)

    n = len(first)
    m = len(second)
    half = max(n, m)/2
    a = first[0:n - half]
    b = first[n - half: n]
    c = second[0:m - half]
    d = second[m - half: n]
    ac = karatsuba_multiplication(a, c)
    middle_temp = karatsuba_multiplication(add_string(a, b), add_string(c, d))
    bd = karatsuba_multiplication(b, d)

    middle = subtract_string(subtract_string(middle_temp, ac), bd)

    shifted_ac = ac + '0'*(2*half)
    shifted_middle = middle + '0'*half
    return add_string(shifted_ac, add_string(shifted_middle, bd))


assert 1234*4567 == int(karatsuba_multiplication("1234", "4567"))
assert 123*12 == int(karatsuba_multiplication("123", "12"))

for index in xrange(10000):
    a = randint(0, 1000000000)
    b = randint(0, 1000000000)
    assert a*b == int(karatsuba_multiplication(str(a), str(b)))