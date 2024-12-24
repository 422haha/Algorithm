lst = [int(input()) for _ in range(6)]
print(sum(sorted(lst[:4])[1:])+max(lst[4:]))