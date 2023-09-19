import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import random
import os

data = pd.read_csv("leads.csv")
leads = data['LeadNumber']
iteration_count = 0


# Check if the file to store sent leads exists, if not create it
sent_leads_file = "sent_leads.txt"
if not os.path.exists(sent_leads_file):
    with open(sent_leads_file, "w") as f:
        pass

# Read the list of previously sent leads from the file
with open(sent_leads_file, "r") as f:
    sent_leads = set(f.read().splitlines())

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
    iteration_count += 1
    if lead in sent_leads:
        continue  # Skip this lead if it has been sent a message before

    sleep_duration = random.choice([30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
    random_message = random.choice(messages_list)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+random_message)
    time.sleep(15)
    
    if first:
        first = False
    
    width, height = pg.size()
    pg.click(width/2, height/2)
    time.sleep(sleep_duration)
    pg.press('enter')
    time.sleep(3)
    pg.hotkey('ctrl', 'w')
    time.sleep(3)

    
    # Mark this lead as sent by adding it to the set of sent leads
    sent_leads.add(lead)
    
    # Save the updated list of sent leads back to the file
    with open(sent_leads_file, "a") as f:
        f.write(lead + "\n")

    print(f"Total Iterations: {iteration_count}")