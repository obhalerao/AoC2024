from math import gcd

lines = [l.strip() for l in open("../input.txt").readlines()]

locs = {}

n = len(lines)
m = len(lines[0])
def good(a):
    global n, m
    i = a[0]
    j = a[1]
    return 0 <= i < n and 0 <= j < m

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            if lines[i][j] not in locs:
                locs[lines[i][j]] = []
            locs[lines[i][j]].append((i, j))

nlocs = set()
for a in locs:
    elems = locs[a]
    for idx in range(len(elems)):
        for idx2 in range(idx+1, len(elems)):
            val1 = elems[idx]
            val2 = elems[idx2]
            diff = (val1[0]-val2[0], val1[1]-val2[1])
            step = gcd(abs(diff[0]), abs(diff[1]))
            if(step == 0):
                step = 1
            am = abs(diff[0])//step
            bm = abs(diff[1])//step
            d0c = 0
            d1c = 0
            if diff[0] < 0:
                d0c = -1
            elif diff[0] > 0:
                d0c = 1
            if diff[1] < 0:
                d1c = -1
            elif diff[1] > 0:
                d1c = 1
            for cand in range(-2*max(n, m)*step, 2*max(n, m)*step, step):
                pcand = (val1[0]+d0c*cand*am, val1[1]+d1c*cand*bm)
                if good(pcand):
                    nlocs.add(pcand)
print(len(nlocs))