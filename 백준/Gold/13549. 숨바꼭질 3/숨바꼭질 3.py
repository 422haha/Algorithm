import sys
from collections import deque

# 입력을 받습니다.
n, k = map(int, sys.stdin.readline().rstrip().split())

# 방문 배열을 초기화합니다.
MAX_POS = 200000
time = [0] * (MAX_POS + 1)

# 시작 지점이 목표 지점과 같은 경우, 0을 출력하고 종료합니다.
if n == k:
    print(0)
    sys.exit(0)

# BFS를 위한 큐를 초기화합니다.
q = deque([n])

# BFS 탐색을 시작합니다.
while q:
    now = q.popleft()

    # 목표 지점에 도달한 경우, 결과를 저장하고 루프를 탈출합니다.
    if now == k:
        res = time[now]
        break

    # 다음 위치를 계산합니다.
    for next_pos in [now - 1, now + 1, now * 2]:
        # 유효한 위치이고 아직 방문하지 않은 위치인 경우
        if 0 <= next_pos <= MAX_POS and time[next_pos] == 0:
            if next_pos == now * 2 and next_pos != 0:
                time[next_pos] = time[now]
                q.appendleft(next_pos)
            else:
                time[next_pos] = time[now] + 1
                q.append(next_pos)

# 결과를 출력합니다.
print(time[k])