prev = float(input())

while True:
    cur = float(input())
    if cur == 999:
        break
    print("%.2f"%(cur-prev))
    prev = cur