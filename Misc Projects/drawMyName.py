#! usr/bin/python3
# drawMyName.py - draws "CODY" using pyautogui.

from pyautogui import dragRel as dragr
from pyautogui import moveRel as mover
import time

def drawMyName():
    time.sleep(5)
    dragr(15, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(-10, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(10, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(-15, 0, duration=0.2)
    dragr(0, -15, duration=0.2)

    mover(17, 0, duration=0.2)

    dragr(15, 0, duration=0.2)
    dragr(0, 15, duration=0.2)
    dragr(-15, 0, duration=0.2)
    dragr(0, -15, duration=0.2)

    mover(5, 5, duration=0.2)

    dragr(5, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(-5, 0, duration=0.2)
    dragr(0, -5, duration=0.2)

    mover(12, -5, duration=0.2)

    dragr(12, 0, duration=0.2)
    dragr(3, 3, duration=0.2)
    dragr(0, 9, duration=0.2)
    dragr(-3, 3, duration=0.2)
    dragr(-12, 0, duration=0.2)
    dragr(0, -15, duration=0.2)
    
    mover(5, 5, duration=0.2)

    dragr(5, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(-5, 0, duration=0.2)
    dragr(0, -5, duration=0.2)

    mover(12, -5, duration=0.2)

    dragr(5, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(5, 0, duration=0.2)
    dragr(0, -5, duration=0.2)
    dragr(5, 0, duration=0.2)
    dragr(0, 10, duration=0.2)
    dragr(-5, 0, duration=0.2)
    dragr(0, 5, duration=0.2)
    dragr(-5, 0, duration=0.2)
    dragr(0, -5, duration=0.2)
    dragr(-5, 0, duration=0.2)
    dragr(0, -10, duration=0.2)



if __name__ == "__main__":
    drawMyName()
