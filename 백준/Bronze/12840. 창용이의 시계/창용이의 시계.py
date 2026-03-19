h, m, s = map(int, input().split())
q = int(input())
cur = h*3600+m*60+s
day = 24*3600

for _ in range(q):
    lst = list(map(int, input().split()))
    t = lst[0]
    if t == 1:
        c = lst[1]
        cur = (cur+c)%day
    elif t == 2:
        c = lst[1]
        cur = (cur-c)%day
    else:
        nh = cur//3600
        nm = (cur%3600)//60
        ns = cur%60
        print(nh, nm, ns)