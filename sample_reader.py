import pickle

def read_sample(filename):
    data = None
    with open(filename,'rb')as f:
        data = pickle.load(f)
    return data