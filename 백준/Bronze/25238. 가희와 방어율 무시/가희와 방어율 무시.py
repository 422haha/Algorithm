import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if b == 0:                      # 방무 0일땐 데미지 0
    print(1)
    sys.exit(0)

ignore = a * (100-b) // 100     # 방무 표기값
if ignore >= 100:
    print(0)
else:
    print(1)