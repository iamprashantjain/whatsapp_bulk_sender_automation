import pywhatkit as kit
import pyautogui as pg
import time
from datetime import datetime, timedelta
import pdb

phone_numbers = ['+919716072106', '+918052340284', '+918052340283']
message = 'Hello World'


current_time = datetime.now()
new_time = current_time + timedelta(seconds=60)
hour = new_time.hour
minute = new_time.minute


# Loop through the list of phone numbers and send messages
for phone_number in phone_numbers:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    time.sleep(15)
    pg.press("enter")
