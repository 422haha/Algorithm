lst = [int(input()) for _ in range(int(input()))]

if lst.index(min(lst)) == 0:
    print("ez")
elif lst.index(max(lst)) == 0:
    print("hard")
else:
    print("?")