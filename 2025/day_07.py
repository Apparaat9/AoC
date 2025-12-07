from functools import cache

M = {complex(i, t) : y for i, x in enumerate(open('input/day_07.txt').read().split()) for t, y in enumerate(x)}
S = [k for k in M if M[k] == 'S'][0]

splits = set()

@cache
def breaks(cur):
    if cur not in M: 
        return 1
    
    if M[cur] == '^':
        splits.add(cur)
        return breaks(cur+1j+1) + breaks(cur-1j+1)
    
    return breaks(cur+1)    

ans = breaks(S+1)
print(len(splits), ans)