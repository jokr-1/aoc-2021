target_x = (128, 160)
target_y = (-142, -88)

def simulate(u, v):
    x, y = 0, 0
    y_high = 0
    while True:
        u, v = min(0, u+1) if u < 0 else max(0, u-1), v-1
        x, y = x+u, y+v
        y_high = max(y_high, y)
        if x > target_x[1] or y < target_y[0]:
            return False, y_high
        if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
            return True, y_high

def solve():
    RANGE = 200
    best = 0
    solutions = set()
    for u in range(0,RANGE):
        for v in range(-RANGE,RANGE,1):
            ok, y_max = simulate(u,v)
            if ok:
                solutions.add((u,v))
                best = max(best, y_max)
    return best, solutions
                
best, solutions = solve()
print("Part 1:", best)
print("Part 2:", len(solutions))