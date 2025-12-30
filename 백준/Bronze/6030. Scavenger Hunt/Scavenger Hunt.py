p, q = map(int, input().split())

p_factors = [i for i in range(1, p+1) if p%i == 0]
q_factors = [j for j in range(1, q+1) if q%j == 0]

for pf in p_factors:
    for qf in q_factors:
        print(pf, qf)