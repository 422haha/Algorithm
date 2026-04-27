import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
# 듣도 못한 사람
nh = {}
for _ in range(n):
    nh[sys.stdin.readline().rstrip()] = 1
# 듣도 보도 못한 사람
nhs = {}
for _ in range(m):
    ns = sys.stdin.readline().rstrip()
    if ns in nh:
        nhs[ns] = 1
# 리스트로 변환 / 정렬 / 출력
lst = []
for i in nhs.keys():
    lst.append(i)
lst = sorted(lst)
print(len(lst))
for i in lst:
    print(i)