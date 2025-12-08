
from math import prod, dist
from collections import defaultdict

d = {tuple(map(int, x.split(','))) for x in open('./input/day_08.txt').read().splitlines()}
distances = {(dist(x,y), *sorted((x, y))) for x in d for y in d if x != y}
circuits = {x : {x} for x in d}

for i, (_, a, b) in enumerate(sorted(distances)):
    new_circuit = circuits[a] | circuits[b]

    if len(new_circuit) == len(d):
        print(a[0]*b[0])
        break

    for k in new_circuit:
        circuits[k] = new_circuit

    if i == 999:
        print(prod(sorted(len(x) for x in {tuple(x) for _, x in circuits.items()})[-3:]))