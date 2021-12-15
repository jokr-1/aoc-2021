with open('input') as f:
    text = [l.rstrip() for l in f.readlines()]

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def check_code(line):
    next = []
    for c in line:
        if c in brackets:
            next.append(brackets[c])
        else:
            e = next.pop()
            if c != e:
                return points[c]
    return 

print('Part 1:', sum(filter(lambda x: not isinstance(x, list), ) for l in text))

def return_expeted(line):
    next = []
    for c in line:
        if c in brackets:
            next.append(brackets[c])
        else:
            e = next.pop()
            if c != e:
                return
    return next

points = {')': 1, ']': 2, '}': 3, '>': 4}
final = []
for l in text:
    e = return_expeted(l)
    if e is not None:
        res = 0
        for c in reversed(e):
            res = res * 5 + points[c]
        final.append(res)

print('Part 2:', sorted(final)[int((len(final)-1)/2)])