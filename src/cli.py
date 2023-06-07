import json

import os

def parse_settings(option: str, settings: dict):
    """
    Finds the correct setting value

    Args:
        option (str): The setting to find
        settings (dict): Contains a dictionary with the settings

    Returns:
        value (var): Associated value for option
        None: Returns None if can't find setting

    """
    
    # Iterate over settings
    for key, value in settings.items():
        
        if key == option:
            return value
    
    return None

def get_settings():
    """
    Loads settings from a json or creates json if it doesn't exist

    Returns:
        settings (dict): Dictionary containing the settings

    """

    # Create placeholder for settings
    settings = {}

    # Check if there is a settings file
    if not os.path.exists("settings.json"):

        # Print diagnostics
        print(f"\n\033[31mNo settings detected\033[0m\n\033[32mCreating settings.json\033[0m")
        # Define default settings
        settings = {
            "user": None,    
            "temperature": 0.5,
            "max_tokens": 2048,
        }

        # Save the json
        with open("settings.json", "w") as file:
            json.dump(settings, file)

    else:
        
        # Print diagnostics
        print(f"\n\033[33mLoading settings\033[0m")

        # Load the json
        with open("settings.json", "r") as file:
            settings = json.load(file)

        # Print diagnostics
        print(f"\n\033[32mSettings loaded\033[0m")

    return settings

def display_settings(settings: dict):
    """
    Displays the settings menu

    Args:
        settings (dict): Contains dictionary of settings

    Returns:
        choice (str): Returns a choice to influence cli

    """
    
    print(f"\n############# SETTINGS ############")

    # Loop over keys and values and print them
    for key, value in settings.items():
        
        print(f"\n{key}: {value}")

    # Prompt options
    choice = input("""
    Select the letter of the option you choose.

    ############# OPTIONS ############
    a) Edit Settings         b) Exit 
    > """)

    return choice

def cli():
    """
    Basic command line interface for the program

    """

    # Load settings
    settings = get_settings()

    # Get name
    name = parse_settings("user", settings)

    # Keeps loop running
    running = True

    # CLI starts
    while(running):

        try:
             # Display welcome message
            choice = int(input(f"""
            ########## POSTFLOW CLI ##########
        
            Hello, {[name if name is not None else "No Name"]}!

        
            Type the number for the option you choose.

            ############# OPTIONS ############

            1) Settings
            
            > """))

            # View settings
            if choice == 1:
                display_settings(settings)

        except:

            print("\n\033[31mWrong option! Try again!\033[0m")
  
