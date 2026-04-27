import sys

t = int(sys.stdin.readline())
for tc in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    if n % h == 0:
        print((n//h) + (h)*100)
    else:
        print(((n//h)+1) + (n % h)*100)