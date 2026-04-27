import sys


def hanoi(level, i, j):             # 현재 단계, 출발 기둥의 번호, 목표 기둥의 번호
    if level == n:  # 목표 층수
        print(i, j)
        return
    else:
        hanoi(level+1, i, 6-i-j)    # 세 기둥의 번호 합은 6
        print(i, j)
        hanoi(level+1, 6-i-j, j)


n = int(sys.stdin.readline())
print(2**n-1)       # 최소 이동 횟수
hanoi(1, 1, 3)