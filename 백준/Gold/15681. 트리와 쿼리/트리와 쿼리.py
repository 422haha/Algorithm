import sys
sys.setrecursionlimit(10**9)


def count_subtree_nodes(node):
    subtree_node_count[node] = 1
    for child in tree[node]:
        if not subtree_node_count[child]:
            count_subtree_nodes(child)
            subtree_node_count[node] += subtree_node_count[child]


# 입력을 받습니다.
n, root, num_queries = map(int, sys.stdin.readline().rstrip().split())
tree = [[] for _ in range(n+1)]
subtree_node_count = [0] * (n+1)

# 트리를 구성합니다.
for _ in range(n-1):
    parent, child = map(int, sys.stdin.readline().rstrip().split())
    tree[parent].append(child)
    tree[child].append(parent)

# 루트에서부터 각 서브트리의 노드 개수를 셉니다.
count_subtree_nodes(root)

# 쿼리를 처리하고 결과를 출력합니다.
for _ in range(num_queries):
    query_node = int(sys.stdin.readline().rstrip())
    print(subtree_node_count[query_node])