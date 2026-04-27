import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
cut = int(sys.stdin.readline())
x_lst = [0, x]
y_lst = [0, y]

for i in range(cut):
    d, n = map(int, sys.stdin.readline().rstrip().split())
    if d == 0:
        y_lst.append(n)
    else:
        x_lst.append(n)

x_lst.sort()
y_lst.sort()
max_ = 0

for i in range(len(x_lst)-1, 0, -1):
    x_lst[i] -= x_lst[i-1]
for i in range(len(y_lst)-1, 0, -1):
    y_lst[i] -= y_lst[i-1]

for i in x_lst:
    for j in y_lst:
        w = i * j
        if w > max_:
            max_ = w

print(max_)