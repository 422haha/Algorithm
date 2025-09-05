n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

res = 0
for i in range(n):
    w = lst[i]*(i+1)
    if w > res:
        res = w
        
print(res)