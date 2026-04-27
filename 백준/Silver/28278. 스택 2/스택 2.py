import sys

t = int(sys.stdin.readline())
stack = []
top = -1

for tc in range(1, t+1):
    lst = list(map(str, sys.stdin.readline().rstrip().split()))
    if lst[0] == '1':
        stack.append(int(lst[1]))
        top += 1
    elif lst[0] == '2':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif lst[0] == '3':
        print(top+1)
    elif lst[0] == '4':
        if top == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == '5':
        if top == -1:
            print(-1)
        else:
            print(stack[top])