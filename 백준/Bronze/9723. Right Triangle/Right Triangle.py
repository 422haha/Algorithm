t = int(input())

for tc in range(1, t+1):
    lst = [i ** 2 for i in [*map(int, input().split())]]
    if max(lst) == sum(lst) - max(lst):
      print(f"Case #{tc}: YES")
    else:
      print(f"Case #{tc}: NO")