n = int(input())
lst = list(map(int, input().split()))
print(min(lst.count(1), lst.count(0)))