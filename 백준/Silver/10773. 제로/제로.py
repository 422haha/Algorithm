import sys

t = int(sys.stdin.readline())

stack = []
top = -1
for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
        top -= 1
    else:
        stack.append(n)
        top += 1
print(sum(stack))