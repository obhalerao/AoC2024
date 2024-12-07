lines = [l.strip() for l in open("../input.txt").readlines()]

def works(res, ops, cur, beg):
    if ops == []:
        return cur == res

    a = None
    b = None
    a = works(res, ops[1:], cur+ops[0], False)
    if a: return a
    b = works(res, ops[1:], cur*ops[0], False)
    if b: return b
    c = works(res, ops[1:], int(str(cur)+str(ops[0])), False)
    if c: return c
    return False
sm = 0
for line in lines:
    a = line.split(':')
    val=int(a[0])
    b = [int(x.strip()) for x in a[1].split()]
    ans = works(val, b[1:], b[0], False)
    if ans:
        sm+=val
print(sm)
