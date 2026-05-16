import pyautogui as pg
import win32api, win32con
import keyboard
import time


# https://www.spelletjes.nl/spel/magische-pianotegels

print("Game has started..")

pg.moveTo(971, 532)
pg.click()

def click_on(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed(' '):
    if pg.pixel(729, 710) == (0, 0, 0):
        print("Tile 1 has been detected!")
        click_on(729, 710)

    elif pg.pixel(857, 710) == (0, 0, 0):
        print("Tile 2 has been detected!")
        click_on(857, 710)

    elif pg.pixel(1014, 710) == (0, 0, 0):
        print("Tile 3 has been detected!")
        click_on(1014, 710)

    elif pg.pixel(1184, 710) == (0, 0, 0):
        print("Tile 4 has been detected!")
        click_on(1184, 710)

"""'
--------------------
FULLSCREEN
START BUTTON = X: 971 Y: 532

TILE 1 = X: 729, Y: 710
TILE 2 = X: 857, Y: 710
TILE 3 = X: 1014, Y: 710
TILE 4 = X: 1184, Y: 710

PIANO NOTE COLOR = RBG(0, 0, 0)
----------------------
MINIMIZED
START BUTTON = X: 735, Y: 453

TILE 1 = X: 609, Y: 609
TILE 2 = X: 689, Y: 609
TILE 3 = X: 770, Y: 609
TILE 4 = X: 843, Y: 609
----------------------
"""