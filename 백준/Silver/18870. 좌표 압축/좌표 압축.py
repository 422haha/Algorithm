import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst_ = sorted(set(lst))
dct = {lst_[i]:i for i in range(len(lst_))}

for i in lst:
    print(dct[i], end=' ')