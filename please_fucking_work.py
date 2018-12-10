import itertools
import tracemalloc

from sample_reader import read_sample


def all_partitions(process, bound):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, bound)]))


def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def idp(coalition):
    solution = []
    counter = 0

    keys = set(coalition.keys())
    max_key = get_max_key(coalition.keys())
    max_len = len(max_key)

    for s in range(2, max_len + 1):
        for c in filter(lambda x: len(x) == s, keys):
            max_value = coalition[c]
            # f1[c] = c
            partitions = all_partitions(c, s // 2 + 1)
            counter += len(partitions)
            for c1 in partitions:
                c2 = tuple(sorted(set(c).difference(set(c1))))
                if max_value < coalition[c1] + coalition[c2]:
                    max_value = coalition[c1] + coalition[c2]
                coalition[c] = max_value

    CS = max_key
    def my_func(cs):

        partitions = all_partitions(cs, len(cs) // 2 + 1)

        for c1 in partitions:
            c2 = tuple(sorted(set(cs).difference(set(c1))))

            if coalition[cs] == coalition[c1] + coalition[c2]:
                solution.append(c1, )

                check = len(solution)
                my_func(c1, )
                if len(solution) != check:
                    solution.remove(c1, )


                solution.append(c2, )
                check = len(solution)
                my_func(c2, )
                if len(solution) != check:
                    solution.remove(c2, )





    my_func(CS)
    print(counter)
    return set(solution), coalition[CS]


input_set = read_sample("10_0_sample")

tracemalloc.start()

print(idp(input_set))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
tracemalloc.stop()

print(top_stats[0])
