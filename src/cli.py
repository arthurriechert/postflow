from settings import get_settings, parse_settings

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
    name = parse_settings(settings, "user")

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
           
            2) End Session
            > """))

            # View settings
            if choice == 1:
                display_settings(settings)

            # End session
            elif choice == 2:
                running = False

        except:

            print("\n\033[31mWrong option! Try again!\033[0m")
  
