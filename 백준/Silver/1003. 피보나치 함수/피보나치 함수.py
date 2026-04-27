import sys

t = int(sys.stdin.readline())

for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    if n == 0:
        print(f'1 0')
        continue
    elif n == 1:
        print(f'0 1')
        continue
    cnt0 = [0] * (n+1)
    cnt1 = [0] * (n+1)
    cnt0[0] = 1
    cnt0[1] = 0
    cnt1[0] = 0
    cnt1[1] = 1
    for i in range(2, n+1):
        cnt0[i] = cnt0[i-1] + cnt0[i-2]
        cnt1[i] = cnt1[i-1] + cnt1[i-2]
    print(cnt0[n], cnt1[n])