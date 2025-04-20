for _ in range(int(input())):
    n = int(input())
    full = n // 5
    remain = n % 5
    result = '++++ ' * full + '|' * remain
    print(result.strip())