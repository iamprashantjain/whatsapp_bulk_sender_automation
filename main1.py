import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pdb
import random


# data = pd.read_csv("leads.csv", delimiter='\t')  # Specify the delimiter as '\t' for tab-separated values

data = pd.read_csv("leads.csv")

data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
combo = zip(leads, messages)
first = True

for lead, message in combo:
    sleep_duration = random.choice([25, 27, 30, 33, 35, 38, 40])
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if first:
        time.sleep(6)
        first = False
    width, height = pg.size()
    pg.click(width/2, height/2)
    time.sleep(sleep_duration)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
    
