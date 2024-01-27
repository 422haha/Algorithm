a, b, c, d, e, f = map(int, input().split())

print(int((c*e-f*b)//(a*e-d*b)), int((c*d-f*a)/(b*d-e*a)))