n = int(input())
lst = [input() for _ in range(n)]
k = int(input())

if k == 1:
    for i in range(n):
        print(lst[i])
elif k == 2:
    for i in range(n):
        print(lst[i][::-1])
else:
    for i in range(n):
        print(lst[n-1-i])