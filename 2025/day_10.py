from itertools import combinations
from scipy.optimize import linprog


r1 = r2 = 0

for t in open('./input/day_10.txt').read().splitlines():
    signal, *opt, seq = t.split()

    signal = [x == "#" for x in signal[1:-1]]
    opt = [eval(f'[{x[1:-1]}]') for x in opt]
    seq = eval(f'[{seq[1:-1]}]')

    def press_all(opt, signal):
        for i in range(1, len(opt)+1):
            for c in combinations(opt, i):
                p = [n for x in c for n in x]
                s = [p.count(x) % 2 for x in range(len(signal))]
                if s == signal:
                    return i
    
    r1 += press_all(opt, signal)

    A_eq = [[1 if i in x else 0 for x in opt] for i in range(len(seq))]
    r2 += linprog(c=[1]*len(opt), A_eq=A_eq, b_eq=seq, integrality=1).fun

print(r1, r2)