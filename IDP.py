import itertools
import tracemalloc

from sample_reader import read_sample

tracemalloc.start()

def all_partitions(process, bound):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, bound)]))


def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def idp(coalition):
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
            max_value = coalition[c]
            f1[c] = c
            partitions = all_partitions(c, s//2 + 1)
            counter += len(partitions)
            for c1 in partitions:
                c2 = tuple(sorted(set(c).difference(set(c1))))
                if max_value < f2[c1] + f2[c2]:
                    max_value = f2[c1] + f2[c2]
                    f1[c] = (c1, c2)
                f2[c] = max_value



    CS = max_key
    find_rec(CS)
    print(counter)
    return solution, f2[CS]

input_set = read_sample("all_samples/18_0_sample")
# file = open("infa.txt", "a")
tracemalloc.start()

print(idp(input_set))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
tracemalloc.stop()
print(top_stats[0])
# file.write(str(top_stats[0]))
# file.write("\n")
# file.close()