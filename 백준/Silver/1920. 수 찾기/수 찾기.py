import sys
def binary_search(lst, num):
    start = 0
    end = len(lst)-1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == num:
            return 1
        elif lst[middle] > num:
            end = middle - 1
        else:
            start = middle + 1
    return 0


n = int(sys.stdin.readline())
lst_n = list(map(int, sys.stdin.readline().rstrip().split()))
lst_n = sorted(lst_n)
m = int(sys.stdin.readline())
lst_m = list(map(int, sys.stdin.readline().rstrip().split()))
for i in lst_m:
    print(binary_search(lst_n, i))