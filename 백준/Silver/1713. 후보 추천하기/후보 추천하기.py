import sys
import heapq

def solution(n):
    student = {}
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    for s in data:
        if s not in student:
            if len(student) >= n:
                min_student = heapq.nsmallest(1, student, key=student.get)
                student.pop(min_student[0])
            student[s] = 1
        else:
            student[s] += 1
    return sorted(student.keys())

n = int(sys.stdin.readline().rstrip())
no = int(sys.stdin.readline().rstrip())
print(*solution(n))