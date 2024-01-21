import sys

num = [0] * 10

for i in range(10):
    n = int(sys.stdin.readline())
    num[i] = n%42

print((len(set(num))))