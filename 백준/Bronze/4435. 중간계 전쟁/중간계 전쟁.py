t = int(input())

gs = [1, 2, 3, 3, 4, 10]
ss = [1, 2, 2, 2, 3, 5, 10]

for b in range(1, t+1):
    gc = list(map(int, input().split()))
    sc = list(map(int, input().split()))
    gt = sum(gc[i]*gs[i] for i in range(6))
    st = sum(sc[i]*ss[i] for i in range(7))
    r = f"Battle {b}: "
    if gt > st:
        r += "Good triumphs over Evil"
    elif st > gt:
        r += "Evil eradicates all trace of Good"
    else:
        r += "No victor on this battle field"  
    print(r)