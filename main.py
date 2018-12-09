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
            temp_values = [
                f2[c_sp] + f2[tuple(sorted(set(c).difference(set(c_sp))))] for
                c_sp in partitions]
            f2[c] = max(temp_values)

            counter += 1
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


#
# input_set = {(1,): 130, (2,): 100, (3,): 60, (4,): 30, (5,): 80, (1, 2): 130,
#              (1, 3): 85, (1, 4): 30, (1, 5): 60, (2, 3): 100, (2, 4): 45,
#              (2, 5): 35, (3, 4): 100, (3, 5): 95, (4, 5): 85, (1, 2, 3): 120,
#              (1, 2, 4): 105, (1, 2, 5): 110, (1, 3, 4): 100, (1, 3, 5): 100,
#              (1, 4, 5): 35, (2, 3, 4): 130, (2, 3, 5): 70, (2, 4, 5): 125,
#              (3, 4, 5): 135, (1, 2, 3, 4): 55, (1, 2, 3, 5): 55,
#              (1, 2, 4, 5): 85, (1, 3, 4, 5): 35, (2, 3, 4, 5): 90,
#              (1, 2, 3, 4, 5): 135}
# print(input_set)

# tracemalloc.start()
# for i in range(3):
#     input_set = read_sample("3_"+str(i)+"_sample")
#     snapshot1 = tracemalloc.take_snapshot()
#     print(dp(input_set))
#     snapshot2 = tracemalloc.take_snapshot()
#     #x = tracemalloc.take_snapshot().statistics('filename')
#     #print(x[0])
#     print(snapshot2.compare_to(snapshot1, "filename")[0])
#
#
# tracemalloc.stop()


input_set = read_sample("19_0_sample")

tracemalloc.start()

print(dp(input_set))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
tracemalloc.stop()

for stat in top_stats:
    print(stat)
