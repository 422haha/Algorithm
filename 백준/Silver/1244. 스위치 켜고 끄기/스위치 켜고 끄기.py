import sys

switch = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
students = int(sys.stdin.readline())

for i in range(students):
    s, n = map(int, sys.stdin.readline().rstrip().split())
    if s == 1:
        for j in range(len(lst)):
            if j % n == 0:
                lst[j] += 1
    if s == 2:
        lst[n] += 1
        k = 1
        while True:
            if n > k and (n+k) <= (len(lst)-1):
                if (lst[n-k]%2) == (lst[n+k]%2):
                    lst[n-k] += 1
                    lst[n+k] += 1
                else:
                    break
            else:
                break
            k += 1

lst = lst[1:]
for i in range(switch):
    lst[i] %= 2

i = -1
while len(lst) // 20 > 0:
    arr = lst[:20]
    lst = lst[20:]
    print(*arr)
print(*lst)