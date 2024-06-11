import sys

while True:
    try:
        n, s, t = map(int, sys.stdin.readline().rstrip().split())
        board = []

        # 보드 설정 입력
        cnt = 0
        while cnt < n:
            temp = list(map(int, sys.stdin.readline().rstrip().split()))
            cnt += len(temp)
            board.extend(temp)

        # DP 테이블 초기화
        dp = [[0] * n for _ in range(t)]

        # 초기값 설정
        for i in range(s):
            dp[0][i] = board[i]

        # DP 테이블 갱신
        for i in range(1, t-1):
            for j in range(n):
                temp = 0 if j == 0 else -float('inf')
                for k in range(1, s+1):
                    if j - k >= 0 and dp[i-1][j-k]:
                        temp = max(temp, dp[i-1][j-k])
                dp[i][j] = temp + board[j]

        # 마지막 턴
        for j in range(n):
            temp = -float('inf')
            for k in range(1, s+1):
                if j - k >= 0:
                    temp = max(temp, dp[-2][j-k])
            dp[-1][j] = temp + board[j]

        # 결과 계산
        res = max(dp[-2][-i] for i in range(1, s+1))
        print(res)

    except:
        sys.exit(0)