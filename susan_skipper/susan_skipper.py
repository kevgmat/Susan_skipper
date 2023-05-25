import cv2
import numpy as np
import pyautogui
import pyautogui as pg
import time

pyautogui.FAILSAFE = True
pg.PAUSE = 0.25

def coordinate(top_left_x, top_left_y, width, height):
    location = [(top_left_x)/2 + (width)/4,(top_left_y)/2 + (height)/4]
    return location

hours = int(input("enter number of hours = "))
interval = 20
skips = hours * (60/interval)
skip_time = 20*60
print("total skips = ", skips)

time.sleep(3)


for i in range(0, int(skips)):
    print("current skip number = ", i)
    time.sleep(skip_time)

    looper = 0
    page_found = False
    while (page_found == False):
        time.sleep(1)
        skip = pg.locateOnScreen('skip.png', confidence=0.9)
        print(skip, looper)
        if skip != None:
            page_found = True
            break
        else:
            looper += 1
        pg.keyDown("command")
        for i in range(0, looper):
            print("hello")
            pg.keyDown("tab")
            pg.keyUp("tab")
        pg.keyUp("command")

    skip = pg.locateOnScreen('skip.png', confidence = 0.9)
    location = coordinate(skip.left, skip.top, skip.width, skip.height)
    pg.moveTo(location[0],location[1], duration = 0.25)
    pg.click()

    reason = pg.locateOnScreen('reason.png',confidence = 0.9)
    location = coordinate(reason.left, reason.top,reason.width, reason.height)
    pg.moveTo(location[0], location[1], duration = 0.25)
    pg.click()

    final_skip = pg.locateOnScreen('final_skip.png',confidence = 0.9)
    location = coordinate(final_skip.left, final_skip.top, final_skip.width, final_skip.height)
    pg.moveTo(location[0], location[1], duration = 0.25)
    pg.click()

print("finished skipping")

