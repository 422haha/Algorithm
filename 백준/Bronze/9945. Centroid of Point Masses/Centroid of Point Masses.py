i = 1
while True :
    smx = 0
    smy = 0
    tm = 0
    n = int(input())
    if n < 0:
        break
    for _ in range(n):
        x, y, m = map(int, input().split())
        smx += x*m
        smy += y*m
        tm += m
    print('Case %d: %.2f %.2f'%(i, smx/tm, smy/tm))
    i += 1
    input()