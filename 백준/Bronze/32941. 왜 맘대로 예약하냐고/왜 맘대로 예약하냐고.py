t, x = map(int, input().split())
n = int(input())
flag = True

for i in range(n):
    _ = int(input())
    lst = list(map(int, input().split()))
    if x not in lst:
        flag = False

print("YES" if flag else "NO")