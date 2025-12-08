
from math import prod
from collections import defaultdict

d = {tuple(map(int, x.split(','))) for x in open('./input/day_08.txt').read().splitlines()}
distances = {(sum(map(lambda x : (x[0] - x[1])**2, zip(x,y))), *sorted((x, y))) for x in d for y in d if x != y}
circuits = {x : {x} for x in d}

for i, v in enumerate(sorted(distances)):
    new_circuit = circuits[v[1]] | circuits[v[2]]

    if len(new_circuit) == len(d):
        print(v[1][0]*v[2][0])
        break

    for k in new_circuit:
        circuits[k] = new_circuit

    if i == 1000:
        print(prod(sorted(len(x) for x in {tuple(x) for _, x in circuits.items()})[-3:]))