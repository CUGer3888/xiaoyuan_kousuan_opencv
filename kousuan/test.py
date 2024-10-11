import pyautogui
import numpy as np
import time
from pynput import keyboard
from pynput.mouse import Controller
import cv2
keyboard = keyboard.Controller()
mouse = Controller()
def write():
    start_x, start_y = 163, 542
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.dragRel(0, 10, duration=0.01)
    pyautogui.mouseUp()
write()