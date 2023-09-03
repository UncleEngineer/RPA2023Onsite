import pyautogui as p
import time


p.click('button1.png',clicks=2)
time.sleep(1)
p.click('button2.png')
time.sleep(1)

for i in range(10):
    p.scroll(-100 * i)
    time.sleep(1)