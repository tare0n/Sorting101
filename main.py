import csv
from csv_sort import select_sorted


def open_csv(filename):
    with open(filename, newline='') as csvfile:
        data = [{key: value for key, value in row.items()}
                for row in csv.DictReader(csvfile, skipinitialspace=True)]
    return data


select_sorted(open_csv("all_stocks_5yr.csv"), sort_columns=['high'], limit=500)

