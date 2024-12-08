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
            na = (val2[0]-diff[0], val2[1]-diff[1])
            nb = (val1[0]+diff[0], val1[1]+diff[1])
            if good(na):
                nlocs.add(na)
            if good(nb):
                nlocs.add(nb)
print(len(nlocs))