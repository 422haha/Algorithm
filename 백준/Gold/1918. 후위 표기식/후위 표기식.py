import sys

str1 = sys.stdin.readline().rstrip()
stack = []
res = ''

for s in str1:
    if s == '(':
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    else:
        res += s
while stack:
    res += stack.pop()

print(res)