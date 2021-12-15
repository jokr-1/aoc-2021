import numpy as np

with open('input') as f:
    heights = np.array([[c for c in line.rstrip()] for line in f], dtype=int)

# part 1
n, m =  heights.shape
framed = np.ones([n+2,m+2], dtype=int)*9  # surround by frame of nines for easy edge handling
framed[1:-1,1:-1] = heights
shifted = lambda dx, dy: framed[1+dx:n+dx+1, 1+dy:m+dy+1]
mask = (heights<shifted(1,0)) & \
       (heights<shifted(-1,0)) & \
       (heights<shifted(0,1)) & \
       (heights<shifted(0,-1))
print('Part 1:', heights[mask].sum() + mask.sum())

# part 2
lowpoints = np.where(mask)
lowpoints = lowpoints[0]+1,lowpoints[1]+1  # lowpoints in framed height-profile

def neighbors(p):
    x,y = p
    return (x+1,y),(x-1,y),(x,y+1),(x,y-1)

def check_point(p):
    val = framed[p]
    if val == 9:
        return 0
    else:
        framed[p] = 9  # mark as 9 to exclude from further lookups
        return 1 + sum(check_point(n) for n in neighbors(p))
    
basins = [check_point(lp) for lp in zip(*lowpoints)]
largest = sorted(basins, reverse=True)
print('Part 2:', np.prod(largest[:3]))