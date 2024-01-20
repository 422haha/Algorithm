n = int(input())
data = input()
a = [int(i) for i in data.split(' ')]
min = min(a)
max = max(a)

print(f'{min} {max}')