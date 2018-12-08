import itertools
import pickle, random


def all_partitions(process):
    return tuple(itertools.chain(
        *[itertools.combinations(process, i) for i in range(1, len(process))]))
def generate_equal(amount):
    filename = str(amount)+'_eq'
    with open(filename, 'wb') as f:
        samp = tuple(j for j in range(amount))
        parts = all_partitions(samp)
        sample = {
        key: 50
        for key in parts}
        sample[samp] = 50
        pickle.dump(sample, f)

def generate():
    filename = '_sample'
    for i in (17, 19, 20):
        for k in range(3):
            with open(str(i) + '_' + str(k) + filename, 'wb') as f:
                samp = tuple(j for j in range(i))
                parts = all_partitions(samp)
                sample = {key:random.randint(10,40)*len(key)+random.randint(0,9) for key in parts}
                sample[samp]= random.randint(10,40)*len(samp)+random.randint(0,9)
                pickle.dump(sample,f)
generate_equal(23)