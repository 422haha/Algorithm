import sys

lst = sys.stdin.readline().rstrip()
stack = []
top = -1
pipe = 0
temp = 0
for i in lst:
    if i == "(":
        stack.append(i)
        top += 1
        temp = 1
    else:
        if temp == 1:
            pipe += top
            top -= 1
            temp = 0
        else:
            stack.pop()
            pipe += 1
            top -= 1
            temp = 0
print(pipe)