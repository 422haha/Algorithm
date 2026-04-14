while True:
    d, rh, rv = map(float, input().split())
    if d == 0 and rh == 0 and rv == 0:
        break
    w = 16*d/337**0.5
    h = 9*w/16
    print(f"Horizontal DPI: {rh/w:.2f}")
    print(f"Vertical DPI: {rv/h:.2f}")