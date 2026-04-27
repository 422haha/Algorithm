import sys

t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1):
    str1 = sys.stdin.readline().rstrip()
    cnt = 0
    now = 0
    while cnt >= 0 and now < len(str1):
        if str1[now] == '(':
            cnt += 1
        else:
            cnt -= 1
        now += 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')
