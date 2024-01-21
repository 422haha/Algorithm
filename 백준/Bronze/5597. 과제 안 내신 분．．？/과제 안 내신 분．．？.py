import sys

num = [0] * 31

for i in range(28):
    n = int(sys.stdin.readline())
    num[n] = 1

not_submit = []

for j in range(1,31):
    if num[j] == 0:
        not_submit.append(j)

not_submit = sorted(not_submit)

for k in not_submit:
    print(k, end='\n')