__author__ = 'mislav'
from random import randint


def merge_sort(a):
    if len(a) == 1:
        return a
    half = len(a)/2
    first_half = merge_sort(a[:half])
    second_half = merge_sort(a[half:])
    result = merge(first_half, second_half)
    return result


def merge(first, second):

    first_index = 0
    second_index = 0
    result = []

    while first_index < len(first) or second_index < len(second):
        if first_index == len(first):
            result.append(second[second_index])
            second_index += 1
            continue

        if second_index == len(second):
            result.append(first[first_index])
            first_index += 1
            continue

        if first[first_index] < second[second_index]:
            result.append(first[first_index])
            first_index += 1
            continue

        result.append(second[second_index])
        second_index += 1

    return result


for index in xrange(1000):
    a = [randint(0, 100000000) for i in xrange(1000)]
    assert sorted(a) == merge_sort(a)

print merge_sort([2,3,1,5,4,7,0])