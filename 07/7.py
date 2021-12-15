import numpy as np

with open('input') as f:
    input = f.readlines()
    crab_positions = np.array(list(map(int,input[0].rstrip().split(','))),dtype=int)

positions = np.array([np.arange(crab_positions.min(), crab_positions.max()+1)], dtype=int).transpose()
distances = abs(crab_positions - positions)

fuel_a = distances.sum(axis=1)
print(int(fuel_a.min()))

fuel_b = ((distances**2+distances)/2).sum(axis=1)
print(int(fuel_b.min()))