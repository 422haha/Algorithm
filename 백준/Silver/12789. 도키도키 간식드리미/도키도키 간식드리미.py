n = int(input())
lst = list(map(int, input().split()))
lst_idx = 0

stack = []
top = -1

goal = list(range(1, n+1))
goal_idx = 0
flag = 1

while flag and goal_idx < n:
    if lst_idx < n and lst[lst_idx] == goal[goal_idx]:
        lst_idx += 1
        goal_idx += 1
    elif top == -1:
        stack.append(lst[lst_idx])
        top += 1
        lst_idx += 1
    elif top > -1:
        if stack[top] == goal[goal_idx]:
            stack.pop()
            top -= 1
            goal_idx += 1
        elif stack[top] > lst[lst_idx]:
            stack.append(lst[lst_idx])
            top += 1
            lst_idx += 1
        else:
            flag = 0
            break
    else:
        flag = 0
        break

if flag == 1:
    print(f'Nice')
else:
    print(f'Sad')