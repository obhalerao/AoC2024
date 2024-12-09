lines = [l.strip() for l in open("../input.txt").readlines()]

val = [int(i) for i in lines[0]]



pos = [-1 for i in range(sum(val))]
idx = 0
file = True
for i in range(len(val)):
    fid = i//2
    for j in range(val[i]):
        if file:
            pos[idx] = fid
        idx+=1
    file = not file

last = len(pos)-1
first = 0
while last > first:
    if(pos[last] == -1):
        last-=1
        continue
    while first < last and pos[first] != -1:
        first+=1
    pos[first] = pos[last]
    pos[last] = -1
    last-=1
    first+=1
sm = 0
for i in range(len(pos)):
    if pos[i] == -1:
        break
    sm+=(i*pos[i])
print(sm)