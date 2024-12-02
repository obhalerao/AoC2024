lines = [l.strip() for l in open("../input.txt").readlines()]

cnt = 0

def safe(arr, idx):
    good = True
    s = arr[:]
    del s[idx]
    incr = True if s[1]-s[0] > 0 else False
    for i in range(len(s)-1):
        if incr != (s[i+1]-s[i] > 0):
            good = False
            break
    for i in range(len(s)-1):
        diff = abs(s[i+1]-s[i])
        if diff < 1 or diff > 3:
            good = False
            break
    return good

for line in lines:
    s = [int(i) for i in line.split()]
    if any(safe(s, i) for i in range(len(s))):
        cnt+=1

print(cnt)