__author__ = 'mislav'


def count_inversion(a):
    n = len(a)
    if n <= 1:
        return {"count": 0, "sorted_arr": a}

    half = n/2
    x = count_inversion(a[:half])
    y = count_inversion(a[half:])
    z = merge(x["sorted_arr"], y["sorted_arr"])

    return {"count": x["count"] + y["count"] + z["count"], "sorted_arr": z["sorted_arr"]}


def merge(first, second):

    first_index = 0
    second_index = 0
    count = 0
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
        count += len(first) - first_index
        second_index += 1

    return {"count": count, "sorted_arr": result}

assert count_inversion([1, 3, 5, 2, 4, 6])["count"] == 3
assert count_inversion([1, 20, 6, 4, 5])["count"] == 5

with open('assignment/IntegerArray.txt') as f:

    lines = f.readlines()
    in_arr = []
    for x in lines:
        in_arr.append(int(x))
    print count_inversion(in_arr)["count"]