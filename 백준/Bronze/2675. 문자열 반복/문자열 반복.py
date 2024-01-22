import sys
t = int(sys.stdin.readline())

for i in range(t):
    str_a, b = sys.stdin.readline().split()
    a = int(str_a)
    for j in range(len(b)):
        print(b[j]*a, end='')
    print()