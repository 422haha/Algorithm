import sys


def mul(a, b):  # 분할 정복을 이용한 거듭제곱
    if b == 1:
        return a%c
    else:
        temp = mul(a, b//2)
        if b % 2 == 0:
            return (temp*temp)%c
        else:
            return (temp*temp*a)%c


a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(mul(a, b))