hour, min = map(int, input().split())
req = int(input())
m = min +req
if m//60 != 0:
    h = hour+m//60
    if h>=24:
        print(h-24, m-(m//60)*60)
    else:
        print(h, m-(m//60)*60)
else:
    print(hour, m)