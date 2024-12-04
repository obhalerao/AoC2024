lines = [l.strip() for l in open("../input.txt").readlines()]

cnt = 0
n = len(lines)
m = len(lines[0])

def check(r, c):
    global lines, cnt, n, m
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    for i in range(4):
        if r+i >= 0 and r+i < n:
            w1.append(lines[r+i][c])
        if c+i >= 0 and c+i < m:
            w2.append(lines[r][c+i])
        if r+i >= 0 and r+i < n and c+i >= 0 and c+i < m:
            w3.append(lines[r+i][c+i])
        if r+i >= 0 and r+i < n and c-i >= 0 and c-i < m:
            w4.append(lines[r+i][c-i])
    if ''.join(w1) == 'XMAS' or ''.join(w1) == 'SAMX':
        cnt+=1
    if ''.join(w2) == 'XMAS' or ''.join(w2) == 'SAMX':
        cnt+=1
    if ''.join(w3) == 'XMAS' or ''.join(w3) == 'SAMX':
        cnt+=1
    if ''.join(w4) == 'XMAS' or ''.join(w4) == 'SAMX':
        cnt+=1


for i in range(len(lines)):
    for j in range(len(lines)):
        check(i,j)

print(cnt)
