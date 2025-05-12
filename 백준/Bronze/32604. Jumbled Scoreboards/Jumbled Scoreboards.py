n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    a1, b1 = arr[i]
    a2, b2 = arr[i+1]
    if a2 < a1 or b2 < b1:
        print("no")
        break
else:
    print("yes")