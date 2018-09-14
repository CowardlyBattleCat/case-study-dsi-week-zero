

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
   """Function to clean 'SalePrice' of a single dictionary. Intended to be passed to clean_data function."""
   out_row = row.copy()
   out_row['SalePrice'] = int(out_row['SalePrice'])
   return out_row
