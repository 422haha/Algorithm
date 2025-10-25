n = int(input())
lst = [input() for _ in range(n)]
for _ in range(int(input())):
    x = int(input())
    print(f'Rule {x}:', lst[x-1] if 0 < x <= n else 'No such rule')