import sys
from collections import deque as dq

t = int(sys.stdin.readline())
deque = dq()
top = -1

for tc in range(1, t+1):
    lst = list(map(str, sys.stdin.readline().rstrip().split()))
    if lst[0] == 'push_front':
        deque.appendleft(int(lst[1]))
        top += 1
    elif lst[0] == 'push_back':
        deque.append(int(lst[1]))
        top += 1
    elif lst[0] == 'pop_front':
        if top == -1:
            print(-1)
        else:
            print(deque.popleft())
            top -= 1
    elif lst[0] == 'pop_back':
        if top == -1:
            print(-1)
        else:
            print(deque.pop())
            top -= 1
    elif lst[0] == 'size':
        print(top + 1)
    elif lst[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if top == -1:
            print(-1)
        else:
            print(deque[0])
    elif lst[0] == 'back':
        if top == -1:
            print(-1)
        else:
            print(deque[top])