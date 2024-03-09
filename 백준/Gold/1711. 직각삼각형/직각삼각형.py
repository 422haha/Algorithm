import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt = 0

for i in range(n-2):                                                    # 5C3
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            p1, p2, p3 = arr[i], arr[j], arr[k]
            temp1 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            temp2 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
            temp3 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
            if temp1 + temp2 + temp3 == 2 * max(temp1, temp2, temp3):   # 피타고라스 정리
                cnt += 1

print(cnt)