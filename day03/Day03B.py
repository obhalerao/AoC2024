import re

lines = [l.strip() for l in open("../input.txt").readlines()]

regex = re.compile("mul\\((\\d+),(\\d+)\\)")
do = re.compile("do\\(\\)")
dont = re.compile("don\'t\\(\\)")
ans = 0
onmul = True
for line in lines:
    nline = line
    res = regex.search(nline)
    dores = do.search(nline)
    dontres = dont.search(nline)
    while (res or dores or dontres):
        mpos = -1
        if dores and ((not res) or (dores.start() < res.start()) and ((not dontres) or dores.start() < dontres.start())):
            onmul = True
            mpos = dores.end()
        elif dontres and ((not dontres) or (dontres.start() < res.start())) and ((not dores) or (dontres.start() < dores.start())):
            onmul = False
            mpos = dontres.end()
        else:
            if onmul:
                prod = (int(res.groups()[0])*int(res.groups()[1]))
                ans+=prod
            mpos = res.end()
        nline = nline[mpos:]
        res = regex.search(nline)
        dores = do.search(nline)
        dontres = dont.search(nline)
print(ans)
