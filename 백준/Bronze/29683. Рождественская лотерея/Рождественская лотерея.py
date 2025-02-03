n, a = map(int, input().split())
print(sum(i//a for i in map(int, input().split())))