t1 = int(input())
t2 = int(input())
res = 2
while True:
    temp = t1-t2
    res += 1
    if temp > t2:
        break
    else:
        t1 = t2
        t2 = temp
print(res)