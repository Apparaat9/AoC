for n, fr in [[2, 0], [12,0]]:
    for row in open('./input/day_03.txt').read().splitlines():
        ris, s = '', 0
        for i in range(n):
            new_max = -(n-i-1) if -(n-i-1) else None
            s = 1 + s + row[s:new_max].index(max(row[s:new_max]))
            ris += row[s - 1]
        fr += int(ris)
    print(fr)