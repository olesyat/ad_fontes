def get_max_length(keys):
    return len(max(keys,key=lambda x: len(x)))


def dp(coalition):
    f = dict()
    max_len = get_max_length(coalition.keys())
    print(max_len)

    partitions=2**max_len-1

    for i in range(1,max_len+1):
            f[(i,)] = coalition[(i,)]

    def helper(i):
        for key in coalition:
            if len(key) == i:
                separate = 0
                new_key = []
                for part in key:
                    separate+=coalition[(part,)]
                    new_key.append((part,))
                if separate < coalition[key]:
                    f[key] = coalition[key]
                else:
                    a = tuple(new_key)
                    f[a] = sum(coalition[(part,)]for part in key)#coalition[(key[0],)] + coalition[(key[1],)]



                # else:
                #     break

    helper(2)
    helper(3)
    # helper(2)
    # helper(3)

    print(f)
    #
    # for key in SET:
    #     if type(key) != int and len(key) == 2:
    #         if SET[key[0]] + SET[key[1]] > SET[key]:
    #             # f[({(key[0]), (key[1])})] = SET[key[0]] + SET[key[1]]
    #             f1.append([{key[0]}, {key[1]}])
    #             f2.append([SET[key[0]] + SET[key[1]]])
    #         else:
    #             f1.append([{key[0], key[1]}])
    #             f2.append([SET[key]])


    # if type(key) == int:
    #     f1.append([{key}])
    #     f2.append([SET[key]])
    # elif len(key) == 2:
    #     # print(key)
    #     if SET[key[0]] + SET[key[1]] > SET[key]:
    #         f1.append([{key[0]}, {key[1]}])
    #         f2.append([SET[key[0]] + SET[key[1]]])
    #     else:
    #         f1.append([{key[0], key[1]}])
    #         f2.append([SET[key]])


    # for i in range(len(f1)):
    #     print(f1[i], f2[i])


input_set = {(1,): 30, (2,): 40, (3,): 25, (4,): 45,
             (1, 2): 50, (1, 3): 60, (1, 4): 80,
             (2, 3): 55, (2, 4): 70, (3, 4): 80,
             (1, 2, 3): 90, (1, 2, 4): 120, (1, 3, 4): 100,
             (2, 3, 4): 115, (1, 2, 3, 4): 140}
# print(input_set)
dp(input_set)
