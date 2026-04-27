import sys
sys.setrecursionlimit(100000000)


def post_order(start, end):
    if start > end:
        return
    mid = end+1
    for i in range(start+1, end+1):
        if pre_order[start] < pre_order[i]:  # 루트 노드보다 큰 값 -> 서브 트리 나뉘는 곳
            mid = i
            break
    post_order(start+1, mid-1)               # 왼쪽 서브 트리
    post_order(mid, end)                     # 오른쪽 서브 트리
    print(pre_order[start])                  # 루트 노드 출력


pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline().rstrip()))    # 전위 순회 결과 input
    except:
        break

post_order(0, len(pre_order)-1)