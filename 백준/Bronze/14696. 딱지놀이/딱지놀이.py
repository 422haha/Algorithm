import sys


def shape(arr):
    lst = [0]*4
    for s in arr:
        if s == 4:
            lst[0] += 1
        elif s == 3:
            lst[1] += 1
        elif s == 2:
            lst[2] += 1
        elif s == 1:
            lst[3] += 1
    return lst


n = int(sys.stdin.readline())

for i in range(n):
    a_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    a_lst.pop(0)
    a_lst = shape(a_lst)
    b_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    b_lst.pop(0)
    b_lst = shape(b_lst)
    flag = 0
    for j in range(4):
        if a_lst[j] != b_lst[j]:
            if a_lst[j] > b_lst[j]:
                print('A')
                flag = 1
                break
            else:
                print('B')
                flag = 1
                break
    if flag == 0:
        print('D')