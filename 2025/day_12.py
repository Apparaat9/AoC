
*_, slots = open('./input/day_12.txt').read().split('\n\n')
r = 0
for eq, *totals in map(str.split, slots.split('\n')):
    r += int(eq[0:2]) * int(eq[3:5]) >= sum(map(int, totals)) * 9
print(r)