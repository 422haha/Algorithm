import sys

m = int(sys.stdin.readline().rstrip())
lst_sum = 0
lst_xor = 0

for i in range(m):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    if temp[0] == 1:
        lst_sum += temp[1]
        lst_xor = lst_xor^temp[1]
    elif temp[0] == 2:
        lst_sum -= temp[1]
        lst_xor = lst_xor^temp[1]
    elif temp[0] == 3:
        print(lst_sum)
    elif temp[0] == 4:
        print(lst_xor)