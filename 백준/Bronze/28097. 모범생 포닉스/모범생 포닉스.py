n = int(input().strip())
lst = list(map(int, input().split()))

res = sum(lst)
if n > 1:
    res += 8*(n-1)

print(res//24, res%24)