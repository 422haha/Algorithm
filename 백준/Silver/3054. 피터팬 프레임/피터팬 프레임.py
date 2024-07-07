import sys

w = sys.stdin.readline().rstrip()
arr = ['.', '.', '#', '.', '.']

for n, i in enumerate(w, 1):
    s = '*' if n % 3 == 0 else '#'
    arr[0] += f'.{s}..'
    arr[1] += f'{s}.{s}.'
    if n % 3 == 0:
        arr[2] = arr[2][:-1] + f'{s}.{i}.{s}'
    else:
        arr[2] += f'.{i}.{s}'
    arr[3] += f'{s}.{s}.'
    arr[4] += f'.{s}..'

for i in arr:
    print(i)