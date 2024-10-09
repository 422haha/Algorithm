def check(arr):
    print("Gnomes:")
    for i in arr:
        if i == sorted(i) or i == sorted(i, reverse=True):
            print("Ordered")
        else:
            print("Unordered")


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

check(arr)