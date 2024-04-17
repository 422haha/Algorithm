import sys


def check(num):
    cnt = 0
    bin_num = bin(num)[2:]
    k = len(bin_num)
    for i in range(k):
        if bin_num[i] == '1':
            temp = k - i - 1
            cnt += lst[temp] + num - 2 ** temp + 1
            num = num - 2 ** temp
    return cnt


a, b = map(int, sys.stdin.readline().rstrip().split())

lst = [0 for _ in range(60)]
for i in range(1, 60):
    lst[i] = 2**(i-1) + 2*lst[i-1]

print(check(b) - check(a-1))