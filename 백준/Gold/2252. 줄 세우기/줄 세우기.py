import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):          # 간선 정보 입력 및 진입 차수 계산
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    visited[b] += 1

lst = deque()               # 위상 정렬을 위한 큐(lst) 초기화
for i in range(1, n + 1):   # 진입 차수가 0인 정점들을 큐에 삽입
    if visited[i] == 0:
        lst.append(i)

while lst:                  # 위상 정렬 수행
    temp = lst.popleft()
    print(temp, end=' ')    # 정점 출력 후 결과 리스트에 추가
    for i in arr[temp]:     # 인접한 정점들의 진입 차수 감소 및 큐에 추가
        visited[i] -= 1
        if visited[i] == 0:
            lst.append(i)
print()