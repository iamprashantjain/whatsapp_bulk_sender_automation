import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import random

data = pd.read_csv("leads.csv")
leads = data['LeadNumber']


messages_list = [
    "https://youtu.be/ZyzTq40DdCg",
    "https://youtu.be/01LO1Y0fCgg",
    "https://youtu.be/ilFQxdekV1U",
    "https://youtu.be/ZgnbZIEXw9U",
    "https://youtu.be/-T62kkKtRUk",
    "https://youtu.be/mTWRLT6kIY8",
    "https://youtu.be/a7-hfZxHiso",
    "https://youtu.be/v_y4KV39_gY",
    "https://youtu.be/m9EG1HrTbwk",
    "https://youtu.be/bg_obF63XzM"
]

first = True

for lead in leads:
    sleep_duration = random.choice([30,31,32,33,34,35,36,37,38,39])
    random_message = random.choice(messages_list)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+random_message)
    time.sleep(15)
    if first:
        time.sleep(6)
        first = False
    width, height = pg.size()
    pg.click(width/2, height/2)
    time.sleep(sleep_duration)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
    time.sleep(5)