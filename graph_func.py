def graph(max_y=10):
    # график для функции x ^ 0,5
    accuracy = 0
    if 0 <= accuracy < max_y / 2 and max_y > 0:
        if accuracy > 0:
            accuracy_num = float('0.' + '0' * (accuracy - 1) + '1')
        y = max_y
        max_len_y = len(str(max_y)) + accuracy + 1
        y = max_y
        print('График функции y = x ^ 0,5\n')
        print(' ' * max_len_y + '\u2191' + '  y')
        pr_x = 0
        pr_y = y
        pre_pr_y = y
        while y > 0:
            x = round(y ** 2, accuracy)
            if y == max_y:
                max_x = x
            if accuracy > 0:
                y = round(y - accuracy_num, accuracy)
                if pr_x != 0:
                    print(str(pre_pr_y) + ' ' * (max_len_y - len(str(pre_pr_y)))
                          + '\u007C' + ' ' * int(x / accuracy_num)
                          + '*' * int(pr_x - x))
            else:
                y = round(y - 1, accuracy)
                if pr_x != 0:
                    print(str(pre_pr_y) + ' '
                          * (max_len_y - len(str(pre_pr_y)))
                          + '\u007C' + ' ' * int(x) + '*' * int(pr_x - x))
            pr_x, pr_y, pre_pr_y = x, y, pr_y
        print(str(pre_pr_y) + ' ' * (max_len_y - len(str(pre_pr_y)))
              + '\u007C' + '*')
        if accuracy > 0:
            print(' ' * max_len_y + '—' * int(max_x / accuracy_num + 1)
                  + '\u2192' + ' x')
        else:
            print(' ' * max_len_y + '—' * int(max_x + 1) + '\u2192' + ' x')
    else:
        print('Введены некорректные значения')
    print('\n\n')
