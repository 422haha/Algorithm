s = input()
for i in s:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i, end='')