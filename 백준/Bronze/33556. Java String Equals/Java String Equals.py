a = input().rstrip()
b = input().rstrip()
if a == "null":
    a = None
if b == "null":
    b = None

try:
    if a is None:
        raise Exception("NullPointerException")
    res1 = (a == b)
    print("true" if res1 else "false")
except Exception as e:
    print("NullPointerException")

try:
    if a is None:
        raise Exception("NullPointerException")
    if b is None:
        res2 = False
    else:
        res2 = (a.lower() == b.lower())
    print("true" if res2 else "false")
except Exception as e:
    print("NullPointerException")
