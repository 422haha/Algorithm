n = int(input())
lst = [int(input()) for _ in range(n)]
print('S' if max(lst) == lst[0] else 'N')