from colours_cfg import colour


def pattern(amount=5, space=0):  # узор
    # amount - количество повторяющихся элементов, space - расстояние между ними
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.black, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 11, end='')
        print(colour.black, end='')
        print(' ' * 2, end='')
        print(colour.white, end='')
        print(' ' * 11, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.black, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 5, end='')
        print(colour.black, end='')
        print(' ' * 2, end='')
        print(colour.white, end='')
        print(' ' * 10, end='')
        print(colour.black, end='')
        print(' ' * 2, end='')
        print(colour.white, end='')
        print(' ' * 5, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.black, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n\n\n', end='')
