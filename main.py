import itertools

def all_partitions(process):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, len(process))]))


def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def dp(coalition):
    #TODO
    solution = []
    def find_rec(coalit):
        print(coalit)
        if f1[coalit] == coalit:
            solution.append(coalit)
            return
        else:
            find_rec(f1[coalit][0]), find_rec(f1[coalit][1])
    #TODO end
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
            if f2[c] >= coalition[c]:
                c_s = partitions[temp_values.index(f2[c])]
                c_s = (c_s, tuple(sorted(set(c).difference(set(c_s)))))
                f1[c] = c_s
            else:
                f1[c] = c
                f2[c] = coalition[c]
    print(f1)
    print(f2)
    CS = max_key
    find_rec(CS)
    return solution,f2[CS]


input_set = {(1,): 30, (2,): 40, (3,): 25, (4,): 45,
             (1, 2): 50, (1, 3): 60, (1, 4): 80,
             (2, 3): 55, (2, 4): 70, (3, 4): 80,
             (1, 2, 3): 90, (1, 2, 4): 120, (1, 3, 4): 100,
             (2, 3, 4): 115, (1, 2, 3, 4): 140}
# print(input_set)
print(dp(input_set))
