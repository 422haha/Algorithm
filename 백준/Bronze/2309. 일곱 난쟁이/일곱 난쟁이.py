import sys

lst = []
for i in range(9):
    lst.append(int(sys.stdin.readline().rstrip()))

sum_ = sum(lst)
flag = 0
for i in range(8):
    for j in range(i+1, 9):
        if flag == 0:
            if (sum_ - lst[i] - lst[j]) == 100:
                flag = 1
                lst.pop(i)
                lst.pop(j-1)
                break
        else:
            break

lst.sort()
for i in lst:
    print(i)