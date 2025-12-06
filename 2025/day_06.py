D = [x for x in open('./input/day_06.txt')]
print(sum(eval(x[-1].join(x[:-1])) for x in zip(*map(str.split, D))))
print(sum(eval(D[-1].split()[i].join([w for w in x if w])) for i, x in enumerate([''.join(y).strip() for y in x] for x in eval(str([*zip(*D[:-1])][:-1]).replace(", (' ', ' ', ' ', ' '),",'],[')))))
