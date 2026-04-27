import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 부분수열의 합을 저장할 리스트를 초기화
l_lst = []
r_lst = []

# 배열을 반으로 나누어 부분수열의 합을 계산
mid = n // 2
l = arr[:mid]
r = arr[mid:]

# 왼쪽 부분 배열의 부분수열의 합을 계산
for i in range(len(l) + 1):
    for comb in combinations(l, i):
        l_lst.append(sum(comb))

# 오른쪽 부분 배열의 부분수열의 합을 계산
for i in range(len(r) + 1):
    for comb in combinations(r, i):
        r_lst.append(sum(comb))

l_lst.sort()
r_lst.sort()

# 두 포인터를 이용하여 합이 S가 되는 경우의 수를 찾음
l = 0
r = len(r_lst) - 1
cnt = 0

while l < len(l_lst) and r >= 0:
    temp = l_lst[l] + r_lst[r]
    if temp == s:
        l_cnt = 1
        r_cnt = 1
        l += 1
        r -= 1
        while l < len(l_lst) and l_lst[l] == l_lst[l - 1]:
            l_cnt += 1
            l += 1
        while r >= 0 and r_lst[r] == r_lst[r + 1]:
            r_cnt += 1
            r -= 1
        cnt += l_cnt * r_cnt
    elif temp < s:
        l += 1
    else:
        r -= 1

# S가 0인 경우 공집합 뺌
if s == 0:
    cnt -= 1

print(cnt)