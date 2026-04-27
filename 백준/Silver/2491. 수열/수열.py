import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

max_increase = 1
max_decrease = 1
arr = []

for i in range(n-1):
    if lst[i] <= lst[i+1]:
        max_increase += 1
    else:
        arr.append(max_increase)
        max_increase = 1
    if lst[i] >= lst[i+1]:
        max_decrease += 1
    else:
        arr.append(max_decrease)
        max_decrease = 1

arr.append(max_increase)
arr.append(max_decrease)
print(max(arr))