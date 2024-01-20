bill = int(input())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    bill -= a*b
if bill == 0:
    print('Yes')
else:
    print('No')