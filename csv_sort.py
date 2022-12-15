import csv
from dict_sort import dicts_quick_sort, additional_sort


def select_sorted(in_data, sort_columns=["high"], limit=30, order='desc', filename='dump.csv'):
    """
    sorts values of all_stocks_5yr.csv
    :param in_data: dict with data from all_stocks_5yr.csv or other file
    :param sort_columns: columns for sorting
    :param limit: limit of highest/lowest values in result
    :param order: 'desc' for descending sort, 'asc' for ascending sort
    :param filename: file for sorted data
    :return: None
    """
    dicts_quick_sort(in_data, sort_columns[0])
    for i in range(1, len(sort_columns)):
        additional_sort(in_data, sort_columns[i], sort_columns[i-1])
    if order == 'desc':
        out_data = in_data[-limit:][::-1]
    elif order == 'asc':
        out_data = in_data[:limit]
    else:
        raise Exception("Incorrect order")
    with open(filename, 'w', newline='') as dump:
        field_names = out_data[0].keys()
        writer = csv.DictWriter(dump, fieldnames=field_names)
        writer.writeheader()
        for coll in out_data:
            writer.writerow(coll)


