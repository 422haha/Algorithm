lv, judgement = input().split()
lv = int(lv)

score_table = {
    "miss": 0,
    "bad": 200*lv,
    "cool": 400*lv,
    "great": 600*lv,
    "perfect": 1000*lv
}

print(score_table[judgement])