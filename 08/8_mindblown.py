basepattern = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"  # 0 1 2 3 4 5 6 7 8 9

def fingerprint(pattern, digit):
    return "".join(sorted([{c: str(pattern.count(c)) for c in "abcdefg"}[d] for d in digit]))

def decode(pattern, digits):
    return  int("".join(translator[fingerprint(pattern, digit)] for digit in digits.split()))

translator = {fingerprint(basepattern, digit): str(i) for i, digit in enumerate(basepattern.split())}

with open('input') as f:
    print(sum(decode(*line.split('|')) for line in f))