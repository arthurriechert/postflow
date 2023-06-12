import json as js

def str_to_json(string: str):
    """
    Converts a string to json format

    Args:
        string (str): Takes a string with json formatting

    Returns:
        json_

    """

    print(f"Here's you STRING: {string}") 

    # Load using json
    json = js.loads(string)

    return json

def list_to_str(list_: list):
    """
    Converts a list to a string

    Args:
        list_ (list): Any flattened list to be converted

    Returns:
        string (str): A string version of the list

    """

    string = ""

    # Iterate and concat
    for element in list_:
        string += element

    print(string)

    return string

def parse_json(json, keys):
    """
    Returns a list containing based on desired keys

    Args:
        key (list or str): Contains desired keys used to find json information
        json (json): Contains data to parse

    Returns:
        results (list): Contains associated values from key

    """

    # Initialize placeholder list
    results = []

    # Recursively iterate over json elements
    if isinstance(json, dict):
        for key, value in json.items():
            if key == keys:
                results.append(value)
            else:
                values = parse_json(value, keys)
                if values: results.append(values)
    elif isinstance(json, list):
        for item in json:
            values = parse_json(item, keys)
            if values: results.append(values)

    return results

def flatten(nested_list):
    """
    Convert a nested list to flat list

    Args:
        nested_list (list): A list containing lists
    
    Returns:
        flattened_list (list): A list not containing lists

    """

    # Initialize placeholder variable
    flattened_list = []

    # Recursively remove dimensions
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)

    return flattened_list

def remove_duplicate_elements(input_list: list):
    """
    Removes duplicate elements from a list by converting it to a set and back

    Args:
        input_list (list): A list contain duplicates

    Returns:
        output_list (list): A list without duplicates

    """

    # Convert list to set and back to list
    output_list = list(set(input_list))

    return output_list


