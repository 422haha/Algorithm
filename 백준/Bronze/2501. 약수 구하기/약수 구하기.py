n, k = map(int, input().split())
lst = []

for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)
long = len(lst)

if long > k-1:
    print(lst[k-1])
else:
    print('0')