n = int(input())
c = 0

for _ in range(n):
    c += int(input())

if c > n-c:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")