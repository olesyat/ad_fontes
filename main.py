def get_max_key(keys):
    return max(keys, key=lambda x: len(x))


def dp(coalition):
    CS = set(coalition.keys())
    f1 = dict()
    f2 = dict()
    max_len = len(get_max_key(coalition.keys()))

    for key in CS:
        if len(key)==1:
            f1[key]=key
            f2[key]=coalition[key]
    for s in range(2,max_len+1):
        for c in coalition:
            if len(c)==s:
                temp_values = []
                for c_sp in range(1,int(0.5*len(c)+1)):
                    temp_values.append()
                f2[c]=max(f2[c[:c_sp]]+f2[c.r])
        # elif len(key) == 2:
        #     if coalition[(key[0],)] + coalition[(key[1],)] < coalition[key]:
        #         f1[key]=key
        #         f2[key]=coalition[key]
        #     else:
        #         f1[key]=((key[0],), (key[1],))
        #         f2[key]=coalition[(key[0],)] + coalition[(key[1],)]

    for s in range(2, max_len):
        for c in coalition:
            if len(c) == s:
                f2[c] = max()

    for c in CS:
        if f1[c] != c:
            CS = CS.remove(c).union({f1[c],})



input_set = {(1,): 30, (2,): 40, (3,): 25, (4,): 45,
             (1, 2): 50, (1, 3): 60, (1, 4): 80,
             (2, 3): 55, (2, 4): 70, (3, 4): 80,
             (1, 2, 3): 90, (1, 2, 4): 120, (1, 3, 4): 100,
             (2, 3, 4): 115, (1, 2, 3, 4): 140}
# print(input_set)
dp(input_set)
