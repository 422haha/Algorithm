lst = list(map(int, input().split()))
print(max(0, 4*lst[4]-sum(lst[:4])))