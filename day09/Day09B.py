lines = [l.strip() for l in open("../input.txt").readlines()]

val = [int(i) for i in lines[0]]
oval = [i for i in val]


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

eidx = len(pos)

last = len(pos)-1
while last >= 0:
    if(pos[last] == -1):
        last-=1
        continue
    ll = last
    while(ll >= 0 and pos[ll] == pos[last]):
        ll-=1
    curblk = last-ll
    cand = 0
    while cand < last:
        if all(pos[i] == -1 for i in range(cand, cand+curblk)):
            break
        cand+=1
    if cand == last:
        last-=curblk
        continue
    for idx in range(curblk):
        pos[cand+idx] = pos[ll+idx+1]
        pos[ll+idx+1] = -1
    last-=curblk
sm = 0
for idx in range(len(pos)):
    if pos[idx] == -1:
        continue
    sm+=(idx*pos[idx])
print(sm)