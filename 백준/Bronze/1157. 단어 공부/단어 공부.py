a = list(input().upper())
b = set(a)
max = 0
bool = False
alpha = 0

for i in b:
    if a.count(i) > max:
        max = a.count(i)
        alpha = i
        bool = True
    elif a.count(i) == max:
        bool = False

if bool == True:
    print(alpha)
else:
    print('?')