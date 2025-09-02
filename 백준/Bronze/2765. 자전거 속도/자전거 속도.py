from math import pi

i = 1
while True:
    d, r, t = map(float, input().split())
    r = int(r)
    if r == 0:
        break
    dis = pi*d*r/63360
    mph = dis/t*3600
    print(f"Trip #{i}: {dis:.2f} {mph:.2f}")
    i += 1