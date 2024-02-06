import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    lst = []
    while n > 0:
        lst.append(n % 10)
        n //= 10
    for i in range(len(lst)//2):
        if lst[i] != lst[len(lst)-1-i]:
            print('no')
            break
    else:
        print('yes')