t1, m1, t2, m2 = map(int, input().split())
t = t2*60+m2-t1*60-m1
t = t+24*60 if t < 0 else t
print(t, t//30)