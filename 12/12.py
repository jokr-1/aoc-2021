with open('input') as f:
    txt = f.readlines()
    pairs = [l.rstrip().split('-') for l in txt]
    nodes = set(n for l in txt for n in l.rstrip().split('-'))
    
edges = {node: set(n for pair in pairs for n in pair if node in pair and n != node) for node in nodes}
small_caves = {n for n in nodes if n.islower()}
big_caves = nodes.difference(small_caves)

def small_visisted(path):
    return any(path.count(n) > 1 for n in small_caves)

def pathfinder(paths):
    new = set()
    for p in paths:
        last = p[-1]
        if last == 'end':
            new.add(p)
            continue
        for dest in edges[last]:
            if (dest not in small_caves) or (dest not in p) or \
               (dest in p and dest not in ('start', 'end') and not small_visisted(p)):
                    new.add((*p, dest))
    if new != paths:
        return pathfinder(new)
    return new


res = pathfinder({('start',)})
print('Part 1:', len(res))