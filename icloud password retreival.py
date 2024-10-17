import pyautogui
import pyperclip
import time
import pandas as pd

def click_copy_button():

    #### INSERT COORDINATES FROM FIND-COORDINATES FILE HERE ####
    pyautogui.click(x=1235, y=54)### <--- INSERT COORDINATES HERE
    time.sleep(1)  

def copy_info(shortcut):
    # Click the copy button before each copy action
    click_copy_button()
    
    # Perform the copy action based on the shortcut
    if shortcut == 'username':
        pyautogui.hotkey('ctrl', 'u')
    elif shortcut == 'password':
        pyautogui.hotkey('ctrl', 'p')
    elif shortcut == 'website':
        pyautogui.hotkey('ctrl', 'w')
    else:
        raise ValueError("Shortcut must be 'username', 'password', or 'website'")
    
    time.sleep(1)  # Wait for the copy action to complete
    return pyperclip.paste()

def extract_passwords(num_entries=134):
    passwords = []
    
    for _ in range(num_entries):
        click_copy_button()  # Click to start with the dropdown menu
        username = copy_info('username')
        password = copy_info('password')
        website = copy_info('website')
        
        entry = {
            'type': 'login',
            'name': website,
            'notes': '',
            'fields': '',
            'tags': '',
            'fav': '',
            'url': website,
            'username': username,
            'password': password,
            'otp': ''
        }
        passwords.append(entry)
        
        # Press the down arrow key to move to the next entry
        pyautogui.press('down')
        time.sleep(1)  # Wait for the entry to change

    return passwords


def save_to_bitwarden_format(passwords, filename='bitwarden_import.csv'):
    # bitwarden import format might be different; this is a placeholder
    df = pd.DataFrame(passwords)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    passwords = extract_passwords()
    save_to_bitwarden_format(passwords)
