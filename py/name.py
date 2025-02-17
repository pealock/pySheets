import pyautogui
from get_data import get_name, wait, text_box, update_led_sign
from pysheets_logo import pysheets_logo
from countdown_timer import countdown_timer

# Get current screen dimensions
screenWidth, screenHeight = pyautogui.size()

# Print pySheets logo
pysheets_logo()

# Sequence loop for fetching new data and updated LED control software
while True:
    # Call data fetch function
    data = get_name()
    names = " - ".join(data) + " - "
    text_box('New data has been fetched.')
    wait(1)
    text_box(f'New list of names: {names}')
    wait(1)
    text_box('Updating LED controller.')
    wait(3)

    # Call update function
    update_led_sign(names, 30, 10)

    # Countdown timer
    countdown_timer(30)





