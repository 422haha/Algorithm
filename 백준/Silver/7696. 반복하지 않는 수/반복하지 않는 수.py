import sys

res = [0] * 26195084
lst = [0] * 1000001

for i in range(10):
    res[i] = (1 << i)
    lst[i] = i

i = 10
idx = 10
while True:
    if res[i//10] == 0:
        i += 1
        continue
    if res[i//10] & res[i%10] == 0:
        res[i] = res[i//10] | res[i%10]
        lst[idx] = i
        idx += 1
    i += 1
    if idx > 1000000:
        break

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    print(lst[n])