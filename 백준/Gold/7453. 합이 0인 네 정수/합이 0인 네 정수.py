import sys

n = int(sys.stdin.readline().rstrip())
a = []
b = []
c = []
d = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    a.append(temp[0])
    b.append(temp[1])
    c.append(temp[2])
    d.append(temp[3])

ab = []
cd = []

for i in a:
    for j in b:
        ab.append(i+j)

for i in c:
    for j in d:
        cd.append(i+j)

ab.sort()
cd.sort()

l = 0
r = n**2-1
cnt = 0

while 0 <= r and l < n**2:
    temp = ab[l] + cd[r]
    if temp < 0:
        l += 1
    elif temp > 0:
        r -= 1
    else:
        x = 1
        for i in range(l+1, n**2):
            if ab[l] == ab[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(r-1, -1, -1):
            if cd[r] == cd[i]:
                y += 1
            else:
                break
        cnt += x*y
        l += x
        r -= y

print(cnt)