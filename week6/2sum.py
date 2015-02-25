__author__ = 'mislav'


def load_hash():
    result = {}
    with open('assignment/algo1_programming_prob_2sum.txt') as f:
        lines = f.readlines()
        for line in lines:
            current = int(line)
            result[current] = 1
    return result


def get_bucket_key(original):
    return original/20000


def two_sum():
    reps_map = load_hash()
    buckets = {}
    for x in reps_map.keys():
        key = get_bucket_key(x)
        bucket = buckets.get(key, {})
        bucket[x] = 1
        buckets[key] = bucket

    found = {}

    for x in buckets.keys():

        active = buckets[x]
        for current in active.keys():
            first_key = get_bucket_key(-10000-current)
            second_key = get_bucket_key(10000-current)

            if first_key in buckets:
                for possible_pair in buckets[first_key].keys():
                    if possible_pair != current and -10000 <= current + possible_pair <= 10000:
                        found[current+possible_pair] = 1
            if second_key in buckets:
                for possible_pair in buckets[second_key].keys():
                    if possible_pair != current and -10000 <= current + possible_pair <= 10000:
                        found[current+possible_pair] = 1


    return len(found)

print two_sum()
