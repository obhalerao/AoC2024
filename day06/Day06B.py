lines = [[i for i in l.strip()] for l in open("../input.txt").readlines()]

def good(r, c):
    global lines
    n = len(lines)
    m = len(lines[0])
    return 0 <= r < n and 0 <= c < m

def go(r, c, guard, gchar):
    global good, lines
    visited = set()
    lines[r][c] = '#'
    ok = False
    while good(*guard):
        if (guard, gchar) in visited:
            ok = True
            break
        visited.add(((guard[0], guard[1]), gchar))
        next = None
        if gchar == 'v':
            next = (guard[0]+1, guard[1])
        elif gchar == '>':
            next = (guard[0], guard[1]+1)
        elif gchar == '^':
            next = (guard[0]-1, guard[1])
        else:
            next = (guard[0], guard[1]-1)
        while good(*next) and lines[next[0]][next[1]] == '#':
            idx = arr.index(gchar)
            gchar = arr[(idx+1)%4]
            if gchar == 'v':
                next = (guard[0]+1, guard[1])
            elif gchar == '>':
                next = (guard[0], guard[1]+1)
            elif gchar == '^':
                next = (guard[0]-1, guard[1])
            else:
                next = (guard[0], guard[1]-1)
        guard = next
    lines[r][c] = '.'
    return ok

arr = ['^', '>', 'v', '<']
guard = None
gchar = None

for idx, i in enumerate(lines):
    for idx2, j in enumerate(i):
        if j == '^' or j == '>' or j == 'v' or j == '<':
            guard = (idx, idx2)
            gchar = j
            break

ans=0
for idx, i in enumerate(lines):
    for idx2, j in enumerate(i):
        if j == '.':
            oguard = (guard[0], guard[1])
            ogchar = gchar
            if go(idx, idx2, oguard, ogchar):
                ans+=1
print(ans)