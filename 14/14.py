with open('input') as f:
    txt = f.readlines()
    seq = txt[0].rstrip()
    mapping = {i:o for l in txt[2:] for (i,o) in [l.rstrip().split(' -> ')]}
    unique = set(c for c in mapping.values())

polymer = {p:[seq[i:i+2] for i in range(len(seq)-1)].count(p) for p in mapping}
counts = {c: seq.count(c) for c in unique}

for i in range(40):
    for p, val in polymer.copy().items():
        insert = mapping[p]
        p1,p2 = p[0]+insert, insert+p[1]
        polymer[p1] += val
        polymer[p2] += val
        polymer[p] -= val
        counts[insert] += val

counts = sorted(counts.values())
print(counts[-1]-counts[0])