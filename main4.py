import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import random
import os

data = pd.read_csv("leads.csv")
leads = data['LeadNumber']
total_leads = len(leads)
iteration_count = 0


pg.FAILSAFE = False


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
start_time = time.time()


for lead in leads:
    iteration_count += 1
    if lead in sent_leads:
        continue

    sleep_duration = random.randint(25,30)
    random_message = random.choice(messages_list)
    time.sleep(2)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+random_message)
    time.sleep(20)
    
    if first:
        first = False
    
    width, height = pg.size()
    pg.click(width/2, height/2)
    time.sleep(sleep_duration)
    pg.press('enter')
    time.sleep(3)
    pg.hotkey('ctrl', 'w')

    # Calculate elapsed time for this lead
    elapsed_time = time.time() - start_time
    
    # Estimate remaining time based on average time per lead
    avg_time_per_lead = elapsed_time / iteration_count
    remaining_leads = total_leads - iteration_count
    estimated_remaining_time = remaining_leads * avg_time_per_lead
    
    # Mark this lead as sent by adding it to the set of sent leads
    sent_leads.add(lead)
    
    # Save the updated list of sent leads back to the file
    with open(sent_leads_file, "a") as f:
        f.write(lead + "\n")

    print(f"Total Iterations: {iteration_count}")
    # print(f"Elapsed Time: {elapsed_time:.2f} seconds")

    estimated_total_time = ((elapsed_time * len(leads))/60)/24
    print(f"Estimated Total Time: {estimated_total_time:.2f} Days")