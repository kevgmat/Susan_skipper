import cv2
import numpy as np
import pyautogui
import pyautogui as pg
import time

pyautogui.FAILSAFE = True
pg.PAUSE = 0.25


def coordinate(top_left_x, top_left_y, width, height):
    location = [(top_left_x) / 2 + (width) / 4, (top_left_y) / 2 + (height) / 4]
    return location


hours = int(input("enter number of hours = "))
interval = 30
skips = hours * (60 / interval)
skip_time = 30 * 60
first_skip_time = int(17.5 * 60)
second_skip_time = int(12.5 * 60)

print("total skips = ", skips)

time.sleep(3)

for i in range(0, int(skips)):
    print("current skip number = ", i)
    # print("|", end = "")
    for i in range(0, first_skip_time):
        if i % 60 == 0:
            print("|", end="")
        time.sleep(1)
    # print("")
    # time.sleep(skip_time)

    looper = 0
    page_found = False
    while (page_found == False):
        time.sleep(1)
        still_here = pg.locateOnScreen('still_here_dark.png', confidence = 0.9)
        if still_here != None:
            page_found = True
            break
        else:
            looper+=1
        pg.keyDown("command")
        for i in range(0, looper):
            pg.keyDown("tab")
            pg.keyUp("tab")
        pg.keyUp("command")
    still_here = pg.locateOnScreen('still_here_dark.png', confidence = 0.9)
    location = coordinate(still_here.left, still_here.top, still_here.width, still_here.height)
    pg.moveTo(location[0], location[1], duration = 0.25)
    pg.click()

    time.sleep(1)
    pg.keyDown("command")
    for i in range(0, looper):
        pg.keyDown("tab")
        pg.keyUp("tab")
    pg.keyUp("command")

    for i in range(0, second_skip_time):
        if i % 60 == 0:
            print("|", end="")
        time.sleep(1)
    print("")

    page_found = False
    looper = 0

    while (page_found == False):
        time.sleep(1)
        skip = pg.locateOnScreen('skip_dark.png', confidence=0.9)
        if skip != None:
            page_found = True
            break
        else:
            looper += 1
        pg.keyDown("command")
        for i in range(0, looper):
            pg.keyDown("tab")
            pg.keyUp("tab")
        pg.keyUp("command")

    skip = pg.locateOnScreen('skip_dark.png', confidence=0.9)
    location = coordinate(skip.left, skip.top, skip.width, skip.height)
    pg.moveTo(location[0], location[1], duration=0.25)
    pg.click()

    reason = pg.locateOnScreen('reason_dark.png', confidence=0.9)
    location = coordinate(reason.left, reason.top, reason.width, reason.height)
    pg.moveTo(location[0], location[1], duration=0.25)
    pg.click()

    final_skip = pg.locateOnScreen('final_skip_dark.png', confidence=0.9)
    location = coordinate(final_skip.left, final_skip.top, final_skip.width, final_skip.height)
    pg.moveTo(location[0], location[1], duration=0.25)
    pg.click()

    time.sleep(1)
    pg.keyDown("command")
    for i in range(0, looper):
        pg.keyDown("tab")
        pg.keyUp("tab")
    pg.keyUp("command")

print("finished skipping")
