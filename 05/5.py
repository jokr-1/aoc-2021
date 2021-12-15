import numpy as np

with open('input') as f:
    input = f.readlines()
    lines = np.array([[tuple(map(int, x.split(','))) for x in l.rstrip().split(' -> ')] for l in input])
    
res = np.zeros([1000,1000])

for l in lines:
    p1, p2 = l
    x1, y1 = p1
    x2, y2 = p2
    n = max(abs(x2-x1), abs(y2-y1)) + 1
    x = np.linspace(x1,x2,n,dtype=int)
    y = np.linspace(y1,y2,n,dtype=int)
    for i in range(n):
        res[x[i],y[i]] += 1
    
print(np.size(res[res>=2]))

pass