h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

res = (3600*h2+60*m2+s2)-(3600*h1+60*m1+s1)
print(res if res > 0 else res+86400)