hour, min = map(int, input().split())
m = min - 45
if m<0:
    h = hour-1
    if h<0:
        print(24+h, 60+m)
    else:
        print(h, 60+m)
else:
    print(hour, m)