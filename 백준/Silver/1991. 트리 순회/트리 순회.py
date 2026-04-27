import sys


def pre_order(n):
    if arr[n][0] != -19:
        print(chr(arr[n][0] + 65), end='')  # 아스키 코드 -> 문자열
    if arr[n][1] != -19:
        pre_order(arr[n][1])
    if arr[n][2] != -19:
        pre_order(arr[n][2])


def in_order(n):
    if arr[n][1] != -19:
        in_order(arr[n][1])
    if arr[n][0] != -19:
        print(chr(arr[n][0] + 65), end='')
    if arr[n][2] != -19:
        in_order(arr[n][2])


def post_order(n):
    if arr[n][1] != -19:
        post_order(arr[n][1])
    if arr[n][2] != -19:
        post_order(arr[n][2])
    if arr[n][0] != -19:
        print(chr(arr[n][0] + 65), end='')


n = int(sys.stdin.readline())
arr = [[-19]*4 for _ in range(n)]

for _ in range(n):
    p, c1, c2 = map(str, sys.stdin.readline().rstrip().split())
    arr[ord(p)-65][0] = ord(p)-65       # 문자열 -> 아스키 코드
    if c1 != '.':
        arr[ord(p)-65][1] = ord(c1)-65
    if c2 != '.':
        arr[ord(p)-65][2] = ord(c2)-65

pre_order(0)
print()
in_order(0)
print()
post_order(0)