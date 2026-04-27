import sys

t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    lst = [i for i in range(1, n+1)]
    for _ in range(k):
        temp = []
        for i in range(n):
            temp.append(sum(lst[:i+1]))
        lst = temp.copy()
    print(lst[-1])