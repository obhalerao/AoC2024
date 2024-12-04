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
    for i in range(3):
        if r+i >= 0 and r+i < n and c+i >= 0 and c+i < m:
            w3.append(lines[r+i][c+i])
        if r+i >= 0 and r+i < n and c-i+2 >= 0 and c-i+2 < m:
            w4.append(lines[r+i][c-i+2])
    if (''.join(w3) == 'MAS' or ''.join(w3) == 'SAM') and (''.join(w4) == 'MAS' or ''.join(w4) == 'SAM'):
        cnt+=1


for i in range(len(lines)):
    for j in range(len(lines)):
        check(i,j)

print(cnt)
