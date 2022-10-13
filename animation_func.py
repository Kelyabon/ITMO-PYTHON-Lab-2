import os
from time import sleep

from colours_cfg import colour


def animation(repeat=1):  # анимация
    # repeat - количество повторений этих двух кадров
    for rep in range(repeat):
        for number in range(1, 4):
            os.system('cls')
            print('|' + colour.white + ' ' * (5 * number) + colour.reset + ' ' * (5 * (3 - number)) + '|')
            sleep(1)
    os.system('cls')

