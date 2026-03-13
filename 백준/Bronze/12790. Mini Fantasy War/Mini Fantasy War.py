for _ in range(int(input())):
    lst = list(map(int, input().split()))
    hp = lst[0]+lst[4]
    mp = lst[1]+lst[5]
    sp = lst[2]+lst[6]
    dp = lst[3]+lst[7]
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if sp < 0:
        sp = 0
    print(1*hp+5*mp+2*sp+2*dp)