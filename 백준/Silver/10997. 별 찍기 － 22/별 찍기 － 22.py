import sys

n = int(sys.stdin.readline().rstrip())

print("*" * (4 * n - 3))

for i in range(n-1):
    sp = " " * (4 * n - 4 * i - 5)
    sb = "* " * (i + 1)
    sa = " *" * i
    print((sb + sp + sa).rstrip())
    print((sb + "*" * (4 * n - 4 * i - 5) + sa).rstrip())

if n != 1:
    mid = "* " * (2 * n - 1)
    print(mid.rstrip())
    print(mid.rstrip())

for i in range(n-1):
    sp = " " * (4 * i + 1)
    sb = "* " * (n - 1 - i)
    sa = " *" * (n - 1 - i)
    print((sb + sp + sa).rstrip())
    sm = "*" * (4 * i + 5)
    sbm = "* " * (n - 2 - i)
    sam = " *" * (n - 2 - i)
    print((sbm + sm + sam).rstrip())