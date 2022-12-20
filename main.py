import csv
from csv_sort import select_sorted, cache_dictionary, get_by_date


def open_csv(filename):
    with open(filename, newline='') as csvfile:
        data = [{key: value for key, value in row.items()}
                for row in csv.DictReader(csvfile, skipinitialspace=True)]
    return data


#select_sorted(open_csv("all_stocks_5yr.csv"), sort_columns=['high'], limit=10)
get_by_date(open_csv("all_stocks_5yr.csv"), date="2015-05-18", name="AAL", filename='dump.csv')