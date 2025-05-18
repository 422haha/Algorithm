def calculate_work_time(start_h, start_m, start_s, end_h, end_m, end_s):
    start_seconds = start_h*3600+start_m*60+start_s
    end_seconds = end_h*3600+end_m*60+end_s
    total_seconds = end_seconds-start_seconds

    h = total_seconds//3600
    m = (total_seconds%3600)//60
    s = total_seconds%60

    return h, m, s

for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    h, m, s = calculate_work_time(sh, sm, ss, eh, em, es)
    print(h, m, s)