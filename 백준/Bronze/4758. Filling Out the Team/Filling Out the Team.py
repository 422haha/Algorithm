while True:
    s, w, st = map(float, input().split())
    if s == 0 and w == 0 and st == 0:
        break
    flag = False
    
    if s <= 4.5 and w >= 150 and st >= 200:
        print("Wide Receiver", end=" ")
        flag = True
    
    if s <= 6.0 and w >= 300 and st >= 500:
        print("Lineman", end=" ")
        flag = True
    
    if s <= 5.0 and w >= 200 and st >= 300:
        print("Quarterback", end=" ")
        flag = True
    
    if not flag:
        print("No positions")
    else:
        print()
