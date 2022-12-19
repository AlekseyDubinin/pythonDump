import csv


def get_by_date(date, name, filename):
    with open('all_stocks_5yr.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'open', 'high', 'low', 'close', 'volume', 'name'])
            for row in reader:
                if row[0] == date and row[6] == name:
                    writer.writerow(row)


get_by_date(date="2013-10-22", name="AAPL", filename='dump.csv')