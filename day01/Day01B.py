lines = [l.strip() for l in open("../input.txt").readlines()]

a = []
b = {}
for line in lines:
    s = line.split()
    a.append(int(s[0].strip()))
    b2 = int(s[1].strip())
    if b2 not in b:
        b[b2] = 0
    b[b2]+=1

sm=0
for i in a:
    if i in b:
        sm+=i*b[i]
print(sm)

