import sys

str_ = list(sys.stdin.readline().strip())
str_bomb = list(sys.stdin.readline().strip())

n = len(str_bomb)
stack = []
for i in str_:
    stack.append(i)
    if stack[len(stack)-n:len(stack)] == str_bomb:
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')