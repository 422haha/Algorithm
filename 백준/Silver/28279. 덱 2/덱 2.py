import sys
from collections import deque as dq

t = int(sys.stdin.readline())
deque = dq()
top = -1

for tc in range(1, t+1):
    lst = list(map(str, sys.stdin.readline().rstrip().split()))
    if lst[0] == '1':
        deque.appendleft(int(lst[1]))
        top += 1
    elif lst[0] == '2':
        deque.append(int(lst[1]))
        top += 1
    elif lst[0] == '3':
        if top == -1:
            print(-1)
        else:
            print(deque.popleft())
            top -= 1
    elif lst[0] == '4':
        if top == -1:
            print(-1)
        else:
            print(deque.pop())
            top -= 1
    elif lst[0] == '5':
        print(top + 1)
    elif lst[0] == '6':
        if top == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == '7':
        if top == -1:
            print(-1)
        else:
            print(deque[0])
    elif lst[0] == '8':
        if top == -1:
            print(-1)
        else:
            print(deque[top])