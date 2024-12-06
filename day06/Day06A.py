lines = [l.strip() for l in open("../input.txt").readlines()]

def good(r, c):
    global lines
    n = len(lines)
    m = len(lines[0])
    return 0 <= r < n and 0 <= c < m

arr = ['^', '>', 'v', '<']

visited = set()
guard = None
gchar = None
for idx, i in enumerate(lines):
    for idx2, j in enumerate(i):
        if j == '^' or j == '>' or j == 'v' or j == '<':
            guard = (idx, idx2)
            gchar = j
            break

while good(*guard):
    visited.add((guard[0], guard[1]))
    next = None
    if gchar == 'v':
        next = (guard[0]+1, guard[1])
    elif gchar == '>':
        next = (guard[0], guard[1]+1)
    elif gchar == '^':
        next = (guard[0]-1, guard[1])
    else:
        next = (guard[0], guard[1]-1)
    if good(*next):
        if lines[next[0]][next[1]] == '#':
            idx = arr.index(gchar)
            gchar = arr[(idx+1)%4]
        else:
            guard = next
    else:
        guard = next
print(len(visited))