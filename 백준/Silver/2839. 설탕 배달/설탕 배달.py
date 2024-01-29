n = int(input())
cnt = 0

if n % 5 == 0:
    print(n//5)
else:
    while n > 0:
        cnt += 1
        n -= 3
        if n % 5 == 0:
            print(cnt + n//5)
            break
    else:
        print(-1)