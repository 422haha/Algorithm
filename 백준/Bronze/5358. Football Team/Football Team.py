while True:
    try:
        while True:
            name = input().strip()
            name = name.replace('i', '#').replace('e', 'i').replace('#', 'e')
            name = name.replace('I', '#').replace('E', 'I').replace('#', 'E')
            print(name)
    except EOFError:
        exit(0)