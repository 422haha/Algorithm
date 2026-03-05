s1, s2 = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(s1)]
lst2 = [list(map(int, input().split())) for _ in range(s2)]

for i in range(s1):
    if lst1[i][0] != lst1[i][1]:
        print("Wrong Answer")
        exit()
for i in range(s2):
    if lst2[i][0] != lst2[i][1]:
        print("Why Wrong!!!")
        exit()
print("Accepted")