import time
import random
import pyautogui

INTERVAL = 50 # in sec movement

print("Jitter running... kill task strg+c.")

try:
    while True:
        pyautogui.moveRel(1, 0)
        pyautogui.movRel(-1, 0)
        time.sleep(INTERVAL + random.randint(-10. 10))
except KeyboardInterrupt:
    print("Paused.")