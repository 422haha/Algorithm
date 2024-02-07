import sys

t = int(sys.stdin.readline())
queue = []
top = -1

for tc in range(1, t+1):
    lst = list(map(str, sys.stdin.readline().rstrip().split()))
    if lst[0] == 'push':
        queue.append(int(lst[1]))
        top += 1
    elif lst[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(queue.pop(0))
            top -= 1
    elif lst[0] == 'size':
        print(top+1)
    elif lst[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if top == -1:
            print(-1)
        else:
            print(queue[0])
    elif lst[0] == 'back':
        if top == -1:
            print(-1)
        else:
            print(queue[top])