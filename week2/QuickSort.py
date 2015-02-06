__author__ = 'mislav'


def get_first_element(input_array, start, end):
    return start


def get_last_element(input_array, start, end):
    return end - 1


def get_median_of_three(input_array,start,end):
    first = input_array[start]
    last = input_array[end-1]
    middle = input_array[(start+end-1)/2]

    if first < middle < last or last < middle < first:
        return (start+end-1)/2

    if middle < last < first or first < last < middle:
        return end-1

    return start


def swap_elements(input_array, first_index, second_index):
    temp = input_array[first_index]
    input_array[first_index] = input_array[second_index]
    input_array[second_index] = temp


def partition(input_array, start, end):

    last_smaller = start + 1
    for x in xrange(start + 1, end):
        if input_array[x] <= input_array[start]:
            swap_elements(input_array, last_smaller, x)
            last_smaller += 1

    swap_elements(input_array, start, last_smaller-1)

    return last_smaller - 1


def quick_sort(input_array, start, end, choose_pivot):

    if (end - start) <= 1:
        return 0

    if start >= len(input_array):
        return 0

    pivot = choose_pivot(input_array, start, end)
    swap_elements(input_array, start, pivot)
    border = partition(input_array, start, end)
    count = end - start - 1
    count += quick_sort(input_array, start, border, choose_pivot)
    count += quick_sort(input_array, border + 1, end, choose_pivot)
    return count


def qs(input_array, pivoting):
    return quick_sort(input_array, 0, len(input_array), pivoting)


def test_qs(input_array, pivoting):
    qs(input_array, pivoting)
    print input_array


def test_partition(in_arr):
    print partition(in_arr, 0, len(in_arr))
    print in_arr

# test_partition([6, 3])
# test_partition([4, 3, 1, 2])

test_qs([2, 3, 1, 5, 4, 7, 9], get_median_of_three)

with open('assignment/QuickSort.txt') as f:

    lines = f.readlines()
    in_arr = []
    for x in lines:
        in_arr.append(int(x))

    # print qs(in_arr, get_first_element)
    # print qs(in_arr, get_last_element)
    print qs(in_arr, get_median_of_three)
