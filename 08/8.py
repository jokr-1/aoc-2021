
with open('input') as f:
    input = f.readlines()
    samples = [[s for s in l.rstrip().split() if s != '|'] for l in input]

res = 0
for probe in samples:
    input, output = probe[:-4], probe[-4:]
    by_length = {i+1: [frozenset(s) for s in input if len(s) == i+1] for i in range(7)}

    # first part
    translator = dict()
    translator[1] = by_length[2][0]  # get 1
    translator[4] = by_length[4][0]  # get 4
    translator[7] = by_length[3][0]  # get 7
    translator[8] = by_length[7][0]  # get 8

    # get 3
    for s in by_length[5]:
        if translator[7].issubset(s):
            translator[3] = s
            by_length[5].remove(s)
            break
        
    # get 5 and 2
    for s in by_length[5]:
        if len(translator[4].difference(s)) == 1:
            translator[5] = s
        else:
            translator[2] = s
    
    # get 9
    for s in by_length[6]:
        if translator[3].issubset(s):
            translator[9] = s
            by_length[6].remove(s)
            break

    # get 0 and 6
    for s in by_length[6]:
        if translator[7].issubset(s):
            translator[0] = s
        else:
            translator[6] = s   

    # count everything
    invert = {v:k for k,v in translator.items()} 
    res += int("".join([str(invert[frozenset(o)]) for o in output]))

print(res)