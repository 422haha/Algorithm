s = input()

if s.startswith('"') and s.endswith('"') and len(s)>2:
    print(s[1:-1])
else:
    print("CE")