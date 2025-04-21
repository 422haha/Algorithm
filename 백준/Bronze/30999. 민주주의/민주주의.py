n, m = map(int, input().split())
half = m//2+1
cnt = 0

for _ in range(n):
    line = input()
    if line.count('O') >= half:
        cnt += 1

print(cnt)