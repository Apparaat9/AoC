ranges, ids = open('./input/day_05.txt').read().split('\n\n')

ranges = [[*map(int, r.split('-'))] for r in ranges.splitlines()]
ids = [*map(int, ids.splitlines())]

for _ in range(2):
    for i, v in enumerate(ranges):
        for x in ranges:
            if x[0] <= v[0] <= x[1]:
                ranges[i][0] = x[0]
            if x[0] <= v[1] <= x[1]:
                ranges[i][1] = x[1]

print(len({id for min, max in ranges for id in ids if min <= id <= max}))
print(sum([y - x + 1 for x, y in set(map(tuple, ranges))]))