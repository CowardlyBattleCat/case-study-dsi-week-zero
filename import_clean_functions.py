

def load_csv_as_dict(file_name_path):
    """Function to take in csv data and return a list of dictionaries with
    header: value as key: value pairs."""
    with open (file_name_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def clean_data(data, cleaning_function):
    """Function to apply a specific cleaning function to data row by row"""
    return [cleaning_function(row) for row in data]

def clean_square_footage(row):
    out_row = row.copy()
    for key, val in out_row.items:
        out_row['SqFtTotLiving'] = int(out_row['SqFtTotLiving'])
    return out_row
