import json




def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data if data else []  # Return an empty list if the file is empty
    except json.decoder.JSONDecodeError:
        return []  # Return an empty list if the file is not valid JSON






def write_json_file(filename, data):
    """Writes data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, default=str)

def get_next_id(data):
    """Returns the next ID for a new item in the given data."""
    if len(data) == 0:
        return 1
    else:
        return data[-1]['id'] +1
    
