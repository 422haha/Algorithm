while True:    
    m, a, b = map(int, input().split())
    if m+a+b == 0:
        break
    t = round((m/a-m/b)*3600)
    h = t//3600
    m = t%3600//60
    s = t%60
    print("%d:%02d:%02d"%(h, m, s))