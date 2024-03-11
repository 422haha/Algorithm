import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

i = 0   # start
j = 1   # mid
k = n-1 # end
res = [0, 0, 0, 3000000000]     # result_i, result_j, result_k, 특성값

while j < k:
    temp = lst[i] + lst[j] + lst[k]
    if res[3] > abs(temp):      # 기존의 특성값 보다 0에 근접
        res = [lst[i], lst[j], lst[k], abs(temp)]
        if temp == 0:
            break
    if temp < 0:
        j += 1
    else:
        k -= 1
    if j >= k:                  # j 값이 k 값 이상일 때 i, j, k 재배치
        i += 1
        j = i + 1
        k = n - 1

print(*res[:3])