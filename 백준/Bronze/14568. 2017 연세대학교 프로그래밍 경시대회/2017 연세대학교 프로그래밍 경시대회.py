n = int(input())
cnt = 0
for i in range(1, (n-2)//2+1):
    for j in range(2, n-i+1):
        k = n-(2*i+j)
        if k > 0 and k%2 == 0:
            cnt += 1
print(cnt)