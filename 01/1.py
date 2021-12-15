with open('input') as f:
    lines = f.readlines()
    numbers = [int(l) for l in lines]

def solve(n):
    packs = [sum(numbers[i:i+n]) for i,_ in enumerate(numbers[:len(numbers)+1-n])]
    res = [int(packs[i+1] > packs[i]) for i, _ in enumerate(packs[:-1])]
    return sum(res)

print(solve(1))  # 1st
print(solve(3))  # 2nd