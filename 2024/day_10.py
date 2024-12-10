M = {complex(i, t) : int(y) for i, x in enumerate(open('input/day_10.txt').read().split()) for t, y in enumerate(x)}

trailheads = [k for k in M if M[k] == 0]

def do_step(current, result):
    if M[current] == 9:
        return [current]
    
    this_result = []
    for next_step in [current + d for d in [1,-1,1j,-1j]]:
        if next_step in M and M[next_step] - M[current] == 1:
            this_result += do_step(next_step, result)

    return this_result

r = [do_step(c, []) for c in trailheads]
print(sum(len(set(x)) for x in r))
print(sum(len(x) for x in r))