from colours_cfg import colour


def poland_flag(length=10, high=1):  # польский флаг
    # length - длина флага, high - высота каждой полоски
    for sth in range(high):
        print(colour.white, end='')
        print(' ' * length, end='')
        print(colour.reset, end='')
        print('\n', end='')
    for sth in range(high):
        print(colour.red, end='')
        print(' ' * length, end='')
        print(colour.reset, end='')
        print('\n', end='')
    print('\n\n', end='')
