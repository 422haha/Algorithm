check = {'l', 'k', 'p'}
s = {input()[0] for _ in range(3)}

if check.issubset(s):
    print("GLOBAL")
else:
    print("PONIX")