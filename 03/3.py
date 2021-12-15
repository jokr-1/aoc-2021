import numpy as np

def l2d(l):
    return sum(2**i*v for i, v in enumerate(reversed(l)))

with open('input') as f:
    input = f.readlines()
    values = np.array([np.array([int(bit) for bit in n.rstrip()], dtype=bool) for n in input])

def most_common(values, invert=False):
    n, m = values.shape
    res = []
    for i in range(m):
        v = values[:,i].sum() >= n/2
        if invert:
            v = not v
        res.append(v)
    return l2d(res)    

def filter_value(values, invert=False):
    n, m = values.shape
    mask = np.ones(n, dtype=bool)
    for i in range(m):
        f = values[mask,i].sum() >= mask.sum()/2
        if invert:
            f = not f
        mask[values[:,i]!=f] = False
        if mask.sum() == 1:
            return l2d(values[mask,:][0])

epsilon = most_common(values, invert=False)
gamma = most_common(values, invert=True)

oxy = filter_value(values, invert=False)
co2 = filter_value(values, invert=True)
print(epsilon*gamma)
print(oxy*co2)
