n = int(input())

i = 1
j = 1
temp = 1
cnt = 0

while i <= n:
    if temp < n:
        j += 1
        temp += j
    elif temp > n:
        temp -= i
        i += 1
    else:
        cnt += 1
        temp -= i
        i += 1

print(cnt)