import csv
import os


def select_sorted(sort_columns, order='asc', limit=10, filename='dump.csv'):
    if order == 'asc':
        order = True
    else:
        order = False
    if os.path.exists(filename):
        print('Результат берется из "кэша", т.к. запрос повторяется с первым.')
    else:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            with open('all_stocks_5yr.csv') as f:
                reader = csv.reader(f)
                header = next(reader)
                writer.writerow(header)
                for row in sorted(reader, key=lambda row: tuple(row[header.index(col)] for col in sort_columns), reverse=order):
                    writer.writerow(row)
                    limit -= 1
                    if limit == 0:
                        break
    with open (filename) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


select_sorted(sort_columns=['high'], order='asc', limit=10, filename='dump1.csv')
select_sorted(sort_columns=['close'], order='asc', limit=10, filename='dump2.csv')
select_sorted(sort_columns=['high'], order='asc', limit=10, filename='dump3.csv')
