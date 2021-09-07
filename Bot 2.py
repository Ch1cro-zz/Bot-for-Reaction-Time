from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(0.5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False: 
    if  pyautogui.pixel(90, 511)[1] == 219:
        click(90, 511)
    time.sleep(0.01)
    if  pyautogui.pixel(90, 511)[2] == 209:
        click(393, 587)
    time.sleep(0.5)
    if  pyautogui.pixel(571, 262)[0] == 255:
        click(431, 497)
    if  pyautogui.pixel(90, 511)[2] == 209:
        click(547, 586)
