lst = list(map(int, input().split()))
print(abs(max(lst)+min(lst)-(sum(lst)-max(lst)-min(lst))))