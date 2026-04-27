import sys
def b_search(arr, num):
    start = 0
    end = arr[-1]
    while start <= end:
        middle = (start + end) // 2
        cnt = 0
        over = 0
        for i in arr:
            if middle < i:
                cnt += i - middle
                over += 1
        if num <= cnt < num + over:
            return middle
        elif cnt >= num + over:
            start = middle + 1
        else:
            end = middle - 1
    return 0

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().split()))
lst = sorted(lst)
print(b_search(lst, m))