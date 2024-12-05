lines = [l.strip() for l in open("../input.txt").readlines()]

edges = []
idx = 0
for line in lines:
    idx+=1
    if line == "":
        break
    s = line.split('|')
    edges.append((int(s[0]), int(s[1])))

sm = 0
for line in lines[idx:]:
    s = [int(i) for i in line.split(',')]
    good = True
    for edge in edges:
        if edge[0] in s and edge[1] in s and s.index(edge[0]) > s.index(edge[1]):
            good = False
            break
    if good:
        sm+=s[len(s)//2]
print(sm)
