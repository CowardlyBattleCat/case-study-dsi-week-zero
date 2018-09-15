import csv

def load_csv_as_dict(file_name_path):
    """Function takes csv data and returns a list of dictionaries with header:
    value as (key: value) pairs."""
    with open (file_name_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def clean_data(data, cleaning_function):
    """Function takes iterable data and applies the specified cleaning function
    to data element by element."""
    return [cleaning_function(row) for row in data if row != None]

def select_cols(row, cols_to_keep):
    """Function takes a dictionary and returns the specified key: value pairs.
    Intended to be passed to clean_data function."""
    return {col: row[col] for col in cols_to_keep}

def combine_major_minor(row):
    """Function merges 'Major' and 'Minor' from one row into a single
    (key: value) pair with key = 'major_minor' and value = a tuple of the
    separate values. Intended to be passed to clean_data function."""
    out_row = row.copy()
    out_row['major_minor'] = tuple((out_row['Major'], out_row['Minor']))
    del out_row['Major']
    del out_row['Minor']
    return out_row

def clean_square_footage(row):
    """Function casts 'SqFtTotLiving' value to integer in a single dictionary
     and removes values of zero. Intended to be passed to clean_data function."""
    out_row = row.copy()
    out_row['SqFtTotLiving'] = int(out_row['SqFtTotLiving'])
    if out_row['SqFtTotLiving'] != 0:
        return out_row

def clean_date(row):
    """Function converts 'DocumentDate' to a two-digit year in a single
    dictionary. Intended to be passed to clean_data function."""
    output = row.copy()
    output['DocumentDate'] = output['DocumentDate'][-4:]
    return output

def clean_sales_price(row):
   """Function casts 'SalePrice' value to integer in a single dictionary.
   Intended to be passed to clean_data function."""
   out_row = row.copy()
   out_row['SalePrice'] = int(out_row['SalePrice'])
   return out_row

def clean_sp_zeros(row):
    """Function removes zeros from 'SalePrice' of a single dictionary.
    Intended to be passed to clean_data function."""
    out_row = row.copy()
    if out_row['SalePrice'] != 0:
        return out_row

def clean_none(row):
    """Function removes empty rows from data. Intended to be passed to
    clean_data function."""
    for val in row.values():
        if val == None:
            break
    else:
        out_row = row.copy()
        return out_row

def clean_none_b(row):
    """Function removes empty rows from data. Intended to be passed to
    clean_data function."""
    if row != None:
        out_row = row.copy()
        return out_row

def clean_none_c(row):
    """Function removes empty rows from data. Intended to be passed to
    clean_data function."""
    if row != None:
        for key in row.keys():
            if row[key] == None:
                break
            else:
                out_row = row.copy()
                return out_row

def clean_none_d(row):
    """Function removes empty rows from data. Intended to be passed to
    clean_data function."""
    if row != None:
        if row['Major'] and row['Minor']:
            out_row = row.copy()
            return out_row

def make_dict_of_dicts(list_of_dicts, unique_id):
    """Function takes a list of dictionaries and returns a dictionary of
    dictionaries with (keys = unique value IDs) and (values = each original
    dictionary). A pair of outputs can be passed to intersection_of_dicts."""
    dod = {}
    for row in list_of_dicts:
        dod[row[unique_id]] = row
    return dod

def intersection_of_dicts(dod1, dod2):
    """Function takes two dictionaries and returns their intersection as a new
    dictionary. Can take outputs from make_dict_of_dicts."""
    dod3 = {}
    for key in (set(dod1) & set(dod2)):
        new_row = dod1[key].copy()
        new_row.update(dod2[key])
        dod3[key] = new_row
    return dod3

def make_list_of_lists(dict_of_dicts):
    """(A not yet working) function to take a dict of dicts as
    input and return a matrix with the first row being a header."""
    matrix = []
    header = list(next(iter(dict_of_dicts.values())).keys())
    matrix.append(header)
    for val_dict in dict_of_dicts.values():
        row = []
        for val in val_dict.values():
            row.append(val)
        matrix.append([row])
    return matrix
