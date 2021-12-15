with open('input') as f:
    energy = [[int(n) for n in l.rstrip()] for l in f]

n,m = len(energy), len(energy[0])
dirs = (-1,-1,-1,0,1,1,1,0),(-1,0,1,1,1,0,-1,-1)

def increase(r,c):
    energy[r][c] += 1
    if energy[r][c] == 10:
        # blink
        blinks = 1
        for dr,dc in zip(*dirs):
            rr,cc = r+dr, c+dc
            if rr in (-1,n) or cc in (-1,m):
                continue
            blinks += increase(rr,cc)
        return blinks
    return 0

step = 1
while True:
    blinks = 0
    for r in range(n):
        for c in range(m):
            blinks += increase(r,c)
    if blinks == n*m:
        print(step, blinks)
        break
    for r in range(n):
        for c in range(m):
            if energy[r][c] > 9:
                energy[r][c] = 0
    step += 1