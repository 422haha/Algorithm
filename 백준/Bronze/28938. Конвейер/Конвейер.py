n = int(input())
lst = list(map(int, input().split()))
res = 0

for i in lst:
    if i == -1:
        res -= 1
    elif i == 1:
        res += 1

if res > 0:
    print("Right")
elif res < 0:
    print("Left")
else:
    print("Stay")