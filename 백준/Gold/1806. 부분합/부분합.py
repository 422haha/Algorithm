import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
res = n+2       # 부분합 길이 임시값 설정

i, j = 0, 0     # i, j 초기값 설정
temp = lst[0]   # 부분합 임시값

while True:
    if temp >= s:
        if res > (j-i+1):
            res = (j-i+1)
        temp -= lst[i]  # 부분합 갱신
        i += 1
    else:
        j += 1
        if j == n:
            break
        temp += lst[j]  # 부분합 갱신

if res == n+2:  # 임시값과 동일하다면 0 출력
    print(0)
else:
    print(res)