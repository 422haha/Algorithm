_ = input()
s = input()

res = ""
for c in s:
    if c == 'J':
        res += 'O'
    elif c == 'O':
        res += 'I'
    elif c == 'I':
        res += 'J'

print(res)