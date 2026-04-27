import sys
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque([n])
res = 0
visited = [0] * 200001
visited[n] = 1
way = [0] * 200001
way[n] = 1

while q:
    now = q.popleft()
    for w in [now-1, now+1, now*2]:
        if 0 <= w <= 200000:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[now]+1
                way[w] += way[now]
            elif visited[w] == visited[now]+1:
                way[w] += way[now]

print(visited[k]-1)
print(way[k])