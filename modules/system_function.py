import os
from datetime import datetime
import modules.data as dta

# Function to clear the terminal screen
def clear_screen():
    # For Unix/Linux/Mac
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

def create_code_orders():
    return f"404_G2U{dta.get_session()['id']}{datetime.now().strftime('%Y%m%d%H%M%S')}"