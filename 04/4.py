import numpy as np

with open('input') as f:
    input = f.readlines()
    sequence = [int(x) for x in input[0].rstrip().split(',')]
    numbers = np.array([int(x) for l in input[1:] if l.rstrip() != '' for x in l.rstrip().split()])
    n = m = 5
    l = int(numbers.size/n/m)
    boards = numbers.reshape(l,n,m)

res = np.zeros(boards.shape,dtype=bool)
winners = dict()
for i, val in enumerate(sequence):
    res[boards==val] = 1
    for idx, b in enumerate(boards):
        r = res[idx]
        v = r.all(axis=0).any()
        h = r.all(axis=1).any()
        if (h or v) and (idx not in winners):
            winners[idx] = b[np.invert(r)].sum() * val

print(winners[list(winners.keys())[0]])  # first
print(winners[list(winners.keys())[-1]])  # last