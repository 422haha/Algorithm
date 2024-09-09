while True:
    name, age, weight = map(str, input().split())
    if name == '#' and age == '0' and weight == '0':
        break
    age = int(age)
    weight = int(weight)
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')