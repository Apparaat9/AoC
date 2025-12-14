from shapely.geometry.polygon import Polygon
from itertools import combinations

d = [eval(x) for x in open('./input/day_09.txt')]
p = Polygon(d)

r1 = r2 = 0
for (w1, h1), (w2, h2) in combinations(d, 2):
    area = (abs(w1 - w2) + 1) * (abs(h1 - h2) + 1)

    w1, w2 = sorted([w1, w2])
    h1, h2 = sorted([h1, h2])
    sp = Polygon([(w1+1,h1+1),(w1+1,h2-1),(w2-1,h1+1),(w2-1,h2-1)])

    if area > r1: r1 = area
    if area > r2 and p.contains(sp): r2 = area
    
print(r1, r2)