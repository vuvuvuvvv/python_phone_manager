import os
from datetime import datetime
import modules.auth as sys_auth

# Function to clear the terminal screen
def clear_screen():
    # For Unix/Linux/Mac
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

def create_code_orders():
    return f"404_G2U{sys_auth.Auth().session_user['id']}{datetime.now().strftime('%Y%m%d%H%M%S')}"