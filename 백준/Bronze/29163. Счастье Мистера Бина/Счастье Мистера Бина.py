n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] % 2 == 0:
        cnt += 1

print("Happy" if cnt > n/2 else "Sad")