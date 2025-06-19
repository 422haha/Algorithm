n, m, k, a, b, c = map(int, input().split())

armies = {
    "Joffrey": n*a,
    "Robb": m*b,
    "Stannis": k*c
}

max_power = max(armies.values())
print(*sorted(name for name, power in armies.items() if power == max_power))
