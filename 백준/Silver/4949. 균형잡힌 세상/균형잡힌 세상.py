import sys

n = sys.stdin.readline().rstrip()
while n != '.':
    stack = []
    top = -1
    flag = 'yes'
    for i in n:
        if i == '(':
            stack.append('(')
            top += 1
        elif i == '[':
            stack.append('[')
            top += 1
        elif i == ')':
            if top > -1:
                temp = stack.pop()
                top -= 1
                if temp != '(':
                    flag = 'no'
                    break
            else:
                flag = 'no'
                break
        elif i == ']':
            if top > -1:
                temp = stack.pop()
                top -= 1
                if temp != '[':
                    flag = 'no'
                    break
            else:
                flag = 'no'
                break
    if top != -1:
        flag = 'no'
    print(flag)
    n = sys.stdin.readline().rstrip()