def convert_unit(value, unit):
    if unit == 'kg':
        return value * 2.2046, 'lb'
    elif unit == 'lb':
        return value * 0.4536, 'kg'
    elif unit == 'l':
        return value * 0.2642, 'g'
    elif unit == 'g':
        return value * 3.7854, 'l'

for _ in range(int(input())):
    value, unit = input().split()
    value = float(value)
    new_value, new_unit = convert_unit(value, unit)
    print(f'{new_value:.4f} {new_unit}')