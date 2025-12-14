d = open('./input/day_01.txt').read().replace('R','').replace('L','-')

a = [50]
z = 0

for i in map(int, d.split()):
    if i < 0 and a[-1]:
        i -= 100

    nr = a[-1] + i
    z += abs(nr) // 100
    a += [nr % 100]

print(a.count(0), z)