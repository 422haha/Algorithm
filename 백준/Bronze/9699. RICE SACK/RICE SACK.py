n = int(input())

for i in range(1, n+1):
    w = list(map(int, input().split()))
    max_w = max(w)
    print(f"Case #{i}: {max_w}")