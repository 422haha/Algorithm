for i in range(int(input())):
    n = int(input())
    lst = [list(map(float, input().split())) for _ in range(n)]
    w = max(i[0] for i in lst)-min(i[0] for i in lst)
    h = max(i[1] for i in lst)-min(i[1] for i in lst)
    print(f"Case {i+1}: Area {w*h}, Perimeter {2*(w+h)}")