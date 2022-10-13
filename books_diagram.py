import csv

from colours_cfg import colour


def diagram(file_path='./books.csv'):
    with open(file_path, 'r') as books_csv:
        books = list(csv.reader(books_csv, delimiter=';'))[1:]
        before = 0
        after = 0
        for book in books:
            year = int(book[6].split('-')[0])
            if year < 2017:
                before += 1
            else:
                after += 1
        percent_before = round(before / len(books) * 100, 2)
        percent_after = round(after / len(books) * 100, 2)
        percent_before_str = str(percent_before) + '%'
        percent_after_str = str(percent_after) + '%'
        int_percent_before = int(percent_before_str.split('.')[0])
        int_percent_after = int(percent_after_str.split('.')[0])
        for number in range(100, 0, -2):
            str_to_print = ''
            if number <= int_percent_before:
                str_to_print += ' ' * 12 + colour.white + '   ' + colour.reset + ' ' * 22
            else:
                str_to_print += ' ' * 37
            if number <= int_percent_after:
                str_to_print += '  ' + colour.white + '   ' + colour.reset + '  '
            else:
                str_to_print += ' ' * 37
            if str_to_print != ' ' * 74:
                print(str_to_print)
        print(' ' * 11 + percent_before_str + ' ' * 21 + percent_after_str)
        print('Книги до 2017 (включительно)     Книги после 2017')
