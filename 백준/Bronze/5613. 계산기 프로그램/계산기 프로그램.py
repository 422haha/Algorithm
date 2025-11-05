res = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+':
        res += n
    elif op == '-':
        res -= n
    elif op == '*':
        res *= n
    elif op == '/':
        res //= n
print(res)