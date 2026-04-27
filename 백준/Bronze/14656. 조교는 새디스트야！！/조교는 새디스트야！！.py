n = int(input())
cnt = 0
lst = list(map(int, input().split()))
for i in range(n): 
    if lst[i] != i+1:
        cnt += 1
print(cnt)