n, m = map(int, input().split())

A = [input()for _ in ' '*n]
input()
B = [input()for _ in ' '*n]

print(sum(A[i][j] == B[i][j] for i in range(n) for j in range(m)))