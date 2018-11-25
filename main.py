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
                c_sps = []
                for c_sp in range(1,int(0.5*len(c)+1)):
                    c_sps.append(c_sp)
                    temp_values.append(f2[c[:c_sp]]+f2[c[c_sp:]])
                f2[c]=max(temp_values)

                if f2[c] >= coalition[c]:
                    c_s = c_sps[temp_values.index(f2[c])]

                    f1[c] = ((c[:c_s],),(c[c_s:],))
                elif f2[c] < coalition[c]:
                    f1[c] = c
                    f2[c] = coalition[c]

  
    for key in f1:
        print(f1[key], f2[key])


    # for c in CS:
    #     if f1[c] != c:
    #         CS = CS.remove(c).union({f1[c],})



input_set = {(1,): 30, (2,): 40, (3,): 25, (4,): 45,
             (1, 2): 50, (1, 3): 60, (1, 4): 80,
             (2, 3): 55, (2, 4): 70, (3, 4): 80,
             (1, 2, 3): 90, (1, 2, 4): 120, (1, 3, 4): 100,
             (2, 3, 4): 115, (1, 2, 3, 4): 140}
# print(input_set)
dp(input_set)
