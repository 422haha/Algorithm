import sys


def calculator(num1, operator, num2):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return int(num1) - int(num2)
    elif operator == '*':
        return int(num1) * int(num2)


def dfs(level, cursum):
    global res
    if level >= n:
        res = max(res, cursum)
        return
    if level < n-1:
        temp = calculator(lst[level*2+2], lst[level*2+3], lst[level*2+4])
        dfs(level+2, calculator(cursum, lst[level*2+1], temp))
    if level < n:
        dfs(level+1, calculator(cursum, lst[level*2+1], lst[level*2+2]))


n = int(sys.stdin.readline().rstrip())
lst = list(map(str, sys.stdin.readline().rstrip()))
if n == 1:
    print(lst[0])
    sys.exit(0)
n //= 2
res = -2**32
dfs(0, int(lst[0]))
print(res)