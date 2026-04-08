temp = 201
s = ''
while True:
    try:
        a, b = input().split()
        b = int(b)
        if b < temp:
            s = a
            temp = b
    except:
        break
print(s)