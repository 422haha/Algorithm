lst = list(map(int, input().split()))
x, y, r = map(int, input().split())

res = 0
if x in lst:
  res = lst.index(x)+1

print(res)