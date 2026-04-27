import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

res = 1             # 만들 수 없는 무게
for i in lst:
    if res < i:     # 지금까지 올린 추 무게의 합보다 올리려는 추의 무게가 더 나가면 break
        break
    res += i

print(res)