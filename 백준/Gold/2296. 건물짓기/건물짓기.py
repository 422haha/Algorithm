import sys


def max_profit(arr):
    # 정렬 기준: x 좌표를 기준으로 오름차순 정렬
    arr.sort(key=lambda x: x[0])

    # DP 테이블 초기화
    dp = [[0, 0] for _ in range(n)]

    # 각 건물의 초기 이익 설정
    for i in range(n):
        dp[i][0] = dp[i][1] = arr[i][2]

    # 다이나믹 프로그래밍을 사용하여 최대 이익 계산
    res = 0
    for i in range(n):
        for j in range(i):
            if arr[j][1] < arr[i][1]:  # 이전 건물보다 y 좌표가 더 큰 경우
                dp[i][0] = max(dp[i][0], dp[j][0] + arr[i][2])
            if arr[j][1] > arr[i][1]:  # 이전 건물보다 y 좌표가 더 작은 경우
                dp[i][1] = max(dp[i][1], dp[j][1] + arr[i][2])
        # 최대 이익 갱신
        res = max(res, dp[i][0], dp[i][1])

    return res


n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 최대 이익 계산 및 출력
res = max_profit(arr)
print(res)