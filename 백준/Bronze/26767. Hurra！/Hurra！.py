for i in range(1, int(input())+1):
    print('Wiwat!' if not i%77 else 'Hurra!' if not i%7 else 'Super!' if not i%11 else i)