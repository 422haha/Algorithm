lst = [list(map(int, input().split())) for _ in range(int(input()))]
arr = sorted(lst, key=lambda x:(-x[0], x[1], x[2]))
print(lst.index(arr[0])+1)