import sys
from collections import deque

n = [i for i in range(1, int(sys.stdin.readline())+1)]
n = deque(n)

while len(n) > 1:
    n.popleft()
    n.append(n.popleft())

print(*n)