"""
Read the data in the included .csv file.
"""

import csv
import json


_FILE = 'data/sic.csv'


def load_data():
    """Load data from the CSV file into memory and return it in various formats.
    """
    data_2007, data_2003 = {}, {}
    with open(_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'SIC 2007' or len(row) != 3: continue
            sic7, sic3, act = row
            if sic7 in data_2007: data_2007[sic7].append(act)
            else: data_2007[sic7] = [ act ]
            if sic3 in data_2003: data_2003[sic3].append(act)
            else: data_2003[sic3] = [ act ]
    return data_2003, data_2007

