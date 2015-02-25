__author__ = 'mislav'

from heapq import heappush, heappop, heappushpop

def load():
    result = []
    with open('assignment/Median.txt') as f:
        lines = f.readlines()
        for line in lines:
            current = int(line)
            result.append(current)
    return result


def find_median():
    input = load()

    max_lower_half = []
    min_upper_half = []
    result = 0

    for x in input:
        active = x
        if len(min_upper_half) > 0 and active > min_upper_half[0]:
            active = heappushpop(min_upper_half, x)

        heappush(max_lower_half, - active)
        if len(max_lower_half) > len(min_upper_half) + 1:
            y = heappop(max_lower_half)
            heappush(min_upper_half, - y)

        result += -max_lower_half[0]

    return result % 10000

print find_median()
