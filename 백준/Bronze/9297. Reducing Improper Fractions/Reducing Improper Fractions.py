t = int(input())
for i in range(1, t+1):
    n, d = map(int, input().split())
    p = n//d
    q = n%d
    print(f"Case {i}:", end=" ")
    if p == 0 and q == 0:
        print(0)
        continue
    if q == 0:
        print(p)
        continue
    if p == 0:
        print(f"{q}/{d}")
    else:
        print(f"{p} {q}/{d}")