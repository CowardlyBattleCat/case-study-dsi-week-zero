

def load_csv_as_dict(file_name_path):
    """Function to take in csv data and return a list of dictionaries with
    header: value as (key: value) pairs."""
    with open (file_name_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def clean_data(data, cleaning_function):
    """Function to apply a specific cleaning function to data row by row."""
    return [cleaning_function(row) for row in data]

def combine_major_minor(row):
    """Function to merge 'Major' and 'Minor' into a single (key: value) pair with
    key = 'major_minor'. Intended to be passed to clean_data function."""
    out_row = row.copy()
    out_row['major_minor'] = tuple((out_row['Major'], out_row['Minor']))
    del out_row['Major']
    del out_row['Minor']
    return out_row

def clean_square_footage(row):
    """Function to clean 'SqFtTotLiving' of a single dictionary. Intended to be
    passed to clean_data function."""
    out_row = row.copy()
    out_row['SqFtTotLiving'] = int(out_row['SqFtTotLiving'])
    return out_row

def clean_date(row):
    """Function to clean 'DocumentDate' of a single dictionary. Intended to be
    passed to clean_data function."""
    output = row.copy()
    output['DocumentDate'] = output['DocumentDate'][-4:]
    return output

def clean_sales_price(row):
   """Function to clean 'SalePrice' of a single dictionary. Intended to be
   passed to clean_data function."""
   out_row = row.copy()
   out_row['SalePrice'] = int(out_row['SalePrice'])
   return out_row

def make_dict_of_dicts(list_of_dicts, unique_id):
    """Function to take a list of dictionaries and return a dictionary of
    dictionaries with (keys = unique value IDs) and (values = each original
    dictionary)."""
    dod = {}
    for row in list_of_dicts:
        dod[row[unique_id]] = row
    return dod

def intersection_of_dicts(dod1, dod2):
    """Function to take two dictionaries and return their intersection as a new
    dictionary."""
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
    header = list(next(dict_of_dicts.values()).keys())
    matrix.append(header)
    for val_dict in dict_of_dicts.keys():
        row = []
        for val in val_dict.keys():
            row.extend(val)
        matrix.append([row])
    return matrix
