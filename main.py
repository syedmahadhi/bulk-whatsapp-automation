import pyautogui as ui
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv("contact.csv")
data_dict = data.to_dict('list')
contact = data_dict['phonenumber']
messages = data_dict['Message']
combo = zip(contact,messages)
first = True
for contact,message in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+contact+"&text="+message)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'q')
