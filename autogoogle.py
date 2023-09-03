import pyautogui as p
import time
import pyperclip
import webbrowser

from datetime import datetime

#1-open web browser (OK)
url = 'https://www.google.com'
#2-goto google.com (OK)
webbrowser.open(url)
time.sleep(2)
# p.hotkey('win','up')

#3-type: 100 baht to jpy (type on keyboard)
keyword = '100 baht to jpy'
p.write(keyword)

#4-press enter (press button)
p.press('enter')
#5-sleep 2 sec
time.sleep(2)
#6-capture and save (capture)

t = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

filename = t + '-' + keyword +'.png'
p.screenshot(filename)

time.sleep(2)
#7-close web browser (short cut)
p.hotkey('alt','f4')

#8-ส่งไลน์ภาพแคปเจอร์ให์ (find library)
from songline import Sendline
token = 'kG89J4K7BxUM5GTynIufN7njtbUPxDH5XSdKgJ5ERf2'
m = Sendline(token)

import os
path = os.getcwd()
filepath = os.path.join(path,filename)
print(filepath)
m.sendimage_file(filepath)







# from PIL import ImageGrab
# filepath = 'my_image.png'
# screenshot = ImageGrab.grab()
# screenshot.save(filepath, 'PNG')

# p.screenshot('C:\\Users\\User\\OneDrive\\Desktop\\Basic Python\\test.png')

'''
p.click(300,300)
time.sleep(1)
p.write('hello',interval=0.25)

thai = 'สวัสดี'
pyperclip.copy(thai)
time.sleep(0.5)
p.hotkey('ctrl','v')
'''