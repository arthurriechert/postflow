import json

import os

def parse_settings(settings, key):
    """
    Returns a list containing based on desired keys

    Args:
        key (list or str): Contains desired keys used to find json information
        json (json): Contains data to parse

    Returns:
        results (list): Contains associated values from key

    """

    # Intialize a placeholder variable
    results = ""

    # Iterate over each setting
    for option, value in settings.items():
        if option == key:
            results = value

    return results

def get_settings():
    """
    Returns a json from settings.json

    Returns:
        settings (json): User configurations

    """

    # Set a placeholder for settings
    settings = {}

    # Check if settings.json exists
    if not os.path.exists("settings.json"):

        # Assembled the settings
        settings = {
            "user": None,
            "temperature": 0.5,
            "max_tokens": 2048,
            "description": "A professional and engaging blog website, with a hint of creativity"
        }

        # Create a new json
        with open("settings.json", 'w') as file:
            json.dump(settings, file)

    else:
        
        # Get the settings
        with open("settings.json", 'r') as file:
            settings = json.load(file)

    return settings

