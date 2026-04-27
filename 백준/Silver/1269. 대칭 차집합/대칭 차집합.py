import sys

num_a, num_b = map(int, sys.stdin.readline().rstrip().split())
a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))
# 대칭 차집합
print(num_a+num_b-int(len(a&b))*2)