import itertools
import tracemalloc

from sample_reader import read_sample


def all_partitions(process, bound):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, bound)]))


def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def idp(coalition):
    f1 = dict()

    keys = set(coalition.keys())
    for key in keys:
        if len(key) == 1:
            f1[key] = key

    solution = []
    counter = 0



    max_key = get_max_key(coalition.keys())
    max_len = len(max_key)


    for s in range(2, max_len + 1):
        for c in filter(lambda x: len(x) == s, keys):
            max_value = coalition[c]
            f1[c] = c
            partitions = all_partitions(c, s // 2 + 1)
            counter += len(partitions)
            for c1 in partitions:
                c2 = tuple(sorted(set(c).difference(set(c1))))
                if max_value < coalition[c1] + coalition[c2]:
                    max_value = coalition[c1] + coalition[c2]
                    coalition[c] = max_value
                    f1[c] = (c1, c2)



    #print(f1)

    print(counter)
    CS = max_key
    def find_rec(coalit):
        if f1[coalit] == coalit:
            solution.append(coalit)
            return
        else:
            find_rec(f1[coalit][0]), find_rec(f1[coalit][1])

    find_rec(CS)
    return (solution), coalition[CS]


input_set = read_sample("17_0_sample")

tracemalloc.start()

print(idp(input_set))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
tracemalloc.stop()

print(top_stats[0])
