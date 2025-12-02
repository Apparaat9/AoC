from itertools import batched
d = map(lambda x : map(int, x.split('-')), open('./input/day_02.txt').read().split(','))

suspects = []
for a,b in d:
    for s in range(a, b+1):
        s = str(s)
        for n in range(1, len(s)):
            if len({*batched(s, n)}) == 1:
                suspects += [(n == len(s) / 2, int(s))]

print(sum(x[1] for x in suspects if x[0]))
print(sum({x[1] for x in suspects}))