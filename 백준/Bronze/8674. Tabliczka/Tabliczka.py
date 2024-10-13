def min_difference(a, b):
    horizontal_first = (a//2)*b
    horizontal_second = (a-a//2)*b
    horizontal_diff = abs(horizontal_first-horizontal_second)

    vertical_first = (b//2)*a
    vertical_second = (b-b//2)*a
    vertical_diff = abs(vertical_first-vertical_second)

    return min(horizontal_diff, vertical_diff)


a, b = map(int, input().split())
print(min_difference(a, b))