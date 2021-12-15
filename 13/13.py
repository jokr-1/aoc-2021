def fold(dots, axis, fold_at):
    fold_map = {'x': lambda x,y: (x if x <= fold_at else 2*fold_at-x, y), 
                'y': lambda x,y: (x, y if y <= fold_at else 2*fold_at-y)}
    return set(fold_map[axis](x,y) for (x,y) in dots)

with open('input') as f:
    dots, instructions = f.read().split('\n\n')
    dots = set(tuple(int(n) for n in d.rstrip().split(',')) for d in dots.split('\n'))
    instructions = [(ax[-1], int(val)) for i in instructions.split('\n') for ax, val in [i.split('=')]]

    for n, (axis, val) in enumerate(instructions):
        dots = fold(dots, axis, val)
        print(n+1, len(dots))

    x_max, y_max = map(max, zip(*dots))
    print("\n".join(" ".join('*' if (x,y) in dots else ' ' for x in range(x_max+1)) for y in range(y_max+1)))