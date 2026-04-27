n, b = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []
new_lst = []

while n > 0:
    lst.append(n % b)
    n = n // b 
lst.reverse()

for i in lst:
    new_lst.append(num[i])

print(''.join(new_lst))