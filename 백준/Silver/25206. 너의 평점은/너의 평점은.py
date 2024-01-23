grade_lst = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_lst = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
score = 0
subject = 0

for i in range(20):
    a, b, c = input().split(' ')
    b = float(b)
    if c != 'P':
        subject += b
        for idx, j in enumerate(grade_lst):
            if j == c:
                score += b * score_lst[idx] 

average = '%0.6f' % (score / subject)
print(average)