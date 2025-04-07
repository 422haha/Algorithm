_ = int(input())
s = list(map(int, input().split()))
s += [0]*(5-len(s))
r = (abs(s[0]-s[2])*(508 if s[0] > s[2] else 108) +
     abs(s[1]-s[3])*(212 if s[1] > s[3] else 305) +
     s[4]*707)
print(r*4763)
