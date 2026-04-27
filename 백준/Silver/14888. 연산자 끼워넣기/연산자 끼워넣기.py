import sys


def dfs(level, sum_, add, sub, mul, div):
    global min_, max_
    if sum_ < int(-1000000000) or int(1000000000) < sum_:
        return
    if level == n:
        min_ = min(min_, sum_)
        max_ = max(max_, sum_)
        return
    if add > 0:   # 연산자 개수 남았을 경우만
        dfs(level+1, sum_+lst[level], add-1, sub, mul, div)
    if sub > 0:
        dfs(level+1, sum_-lst[level], add, sub-1, mul, div)
    if mul > 0:
        dfs(level+1, sum_*lst[level], add, sub, mul-1, div)
    if div > 0:
        dfs(level+1, int(sum_/lst[level]), add, sub, mul, div-1)


n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
add, sub, mul, div = map(int, sys.stdin.readline().rstrip().split())

min_ = 1000000000
max_ = -1000000000
dfs(1, lst[0], add, sub, mul, div)
print(max_)
print(min_)