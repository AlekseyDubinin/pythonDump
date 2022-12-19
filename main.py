import csv


def select_sorted(sort_columns, limit, group_by_name, order, filename):
    with open('dump2/all_stocks_5yr.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    if group_by_name:
        data = sorted(data, key=lambda x: x['Name'])
    for column in sort_columns:
        data = sorted(data, key=lambda x: x[column], reverse=order == 'desc')
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data[:limit]:
            writer.writerow(row)


select_sorted(sort_columns=["high"], limit=10, group_by_name=True, order='asc', filename='dump.csv')
