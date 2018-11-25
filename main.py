def dp(SET):
    f1 = []
    f2 = []
    f = dict()
    n = 0
    for i, key in enumerate(SET):
        print(i+1, key)
        if key == i+1:
            f[frozenset({key})] = SET[key]
            f1.append([{key}])
            f2.append([SET[key]])

        else:
            n = i
            break
    #
    # for key in SET:
    #     if type(key) != int and len(key) == 2:
    #         if SET[key[0]] + SET[key[1]] > SET[key]:
    #             # f[frozenset({frozenset(key[0]), frozenset(key[1])})] = SET[key[0]] + SET[key[1]]
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


    print(f)
    # for i in range(len(f1)):
    #     print(f1[i], f2[i])
input_set = {frozenset((1,)): 30, frozenset((2,)): 40, frozenset((3,)): 25, frozenset((4,)): 45,
             frozenset(((1, 2),)): 50, frozenset(((1, 3),)): 60, frozenset(((1, 4),)): 80,
             frozenset(((2, 3),)): 55, frozenset(((2, 4),)): 70, frozenset(((3, 4),)): 80,
             frozenset(((1, 2, 3),)): 90, frozenset(((1, 2, 4),)): 120, frozenset(((1, 3, 4),)): 100,
             frozenset(((2, 3, 4),)): 115, frozenset(((1, 2, 3, 4),)): 140}
dp(input_set)
