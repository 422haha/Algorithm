import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

i = 0   # start
j = n-1 # end
res = [0, 0, 2000000000]    # result_i, result_j, 특성값

while i < j:
    temp = lst[i] + lst[j]
    if res[2] > abs(temp):       # 기존의 특성값 보다 0에 근접
        res = [lst[i], lst[j], abs(temp)]
        if temp == 0:
            break
    if temp < 0:
        i += 1
    else:
        j -= 1

print(*res[:2])