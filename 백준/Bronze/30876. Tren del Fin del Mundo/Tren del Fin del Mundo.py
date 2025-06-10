n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

print(*min(arr, key=lambda x: x[1]))