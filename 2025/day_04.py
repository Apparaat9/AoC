rolls = {complex(i, t) for i, x in enumerate(open('input/day_04.txt').read().split()) for t, y in enumerate(x) if y == '@'}
surroundings = (-1j, -1-1j, -1, -1+1j, 1j, 1+1j, 1, 1-1j)
removed = set()

for i in range(100):
    for roll in rolls - removed:
        sus = {roll + x for x in surroundings}
        if len(sus & rolls) < 4:
            removed.add(roll)
    rolls -= removed
    if not i: print(len(removed))
print(len(removed))


