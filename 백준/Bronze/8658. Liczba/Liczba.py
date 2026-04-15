n = int(input())

for i in range(2, n+1):
    if n%i != 0:
        print(i, end=" ")
        break
for i in range(1, n+1):
    if n%(n-i) != 0:
        print(n-i)
        break