lines = [l.strip() for l in open("../input.txt").readlines()]

a = []
b = []
for line in lines:
    s = line.split()
    a.append(int(s[0].strip()))
    b.append(int(s[1].strip()))

a.sort()
b.sort()
sm=0
for x,y in zip(a,b):
    sm+=abs(x-y)
print(sm)