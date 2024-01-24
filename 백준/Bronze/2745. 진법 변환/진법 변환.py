n, b = input().split()
rvs_n = ''.join(reversed(n))
b = int(b)
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum_n = 0

for idx, i in enumerate(rvs_n):
    sum_n += b ** idx * num.index(i)

print(sum_n)