with open('input') as f:
    input = f.readlines()
    instructions = [(l.rstrip().split(' ')[0].upper(), int(l.rstrip().split(' ')[1])) for l in input]

h = 0
d = 0
aim = 0
for i, val in instructions:
    if i == 'FORWARD':
        h += val
        d += aim * val
    elif i == 'DOWN':
        aim += val
    elif i == 'UP':
        aim -= val

print(h, d, h*d)