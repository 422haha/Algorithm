n = int(input())
t, w = list(map(int, input().split())), [list(map(int, input().split())) for _ in range(n)]
print(sum(max(0, y-x) for i, (x, y) in enumerate(w) if t[i]))