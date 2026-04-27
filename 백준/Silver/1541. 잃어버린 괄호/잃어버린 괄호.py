import sys

lst_str1 = list(sys.stdin.readline().rstrip().split('-'))
res = sum(map(int, lst_str1[0].split('+')))

for item in lst_str1[1:]:
    res -= sum(map(int, item.split('+')))
print(res)