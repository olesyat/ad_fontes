import itertools
import tracemalloc
from sample_reader import read_sample


def all_partitions(process):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, len(process))]))


def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def dp(coalition):
    solution = []
    counter = 0

    def find_rec(coalit):
        if f1[coalit] == coalit:
            solution.append(coalit)
            return
        else:
            find_rec(f1[coalit][0]), find_rec(f1[coalit][1])

    keys = set(coalition.keys())
    f1 = dict()
    f2 = dict()
    max_key = get_max_key(coalition.keys())
    max_len = len(max_key)

    for key in keys:
        if len(key) == 1:
            f1[key] = key
            f2[key] = coalition[key]

    for s in range(2, max_len + 1):
        for c in filter(lambda x: len(x) == s, keys):
            partitions = all_partitions(c)
            len(partitions)
            temp_values = [
                f2[c_sp] + f2[tuple(sorted(set(c).difference(set(c_sp))))] for
                c_sp in partitions]
            f2[c] = max(temp_values)

            if f2[c] >= coalition[c]:
                c_s = partitions[temp_values.index(f2[c])]
                c_s = (c_s, tuple(sorted(set(c).difference(set(c_s)))))
                f1[c] = c_s
            else:
                f1[c] = c
                f2[c] = coalition[c]
    CS = max_key
    find_rec(CS)
    print(counter)
    return solution, f2[CS]


input_set = read_sample("19_0_sample")

tracemalloc.start()

print(dp(input_set))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
tracemalloc.stop()

for stat in top_stats:
    print(stat)
