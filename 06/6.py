with open('input') as f:
    input = list(map(int, f.readlines()[0].split(',')))
    fishs = [input.count(i) for i in range(9)]

def calc(current, n_days):
    for _ in range(n_days):
        next = [*current[1:], current[0]]  # rollover
        next[6] += current[0]
        current = next
    return sum(current)
    
print(calc(fishs, 80))  # 1st
print(calc(fishs, 256))  # 2nd