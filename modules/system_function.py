import os

# Function to clear the terminal screen
def clear_screen():
    # For Unix/Linux/Mac
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')