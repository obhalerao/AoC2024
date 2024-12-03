import re

lines = [l.strip() for l in open("../input.txt").readlines()]

regex = re.compile("mul\\((\\d+),(\\d+)\\)")
ans = 0
for line in lines:
    nline = line
    res = regex.search(nline)
    while res:
        prod = (int(res.groups()[0])*int(res.groups()[1]))
        ans+=prod
        print(res.end())
        nline = nline[res.end():]
        res = regex.search(nline)
print(ans)
