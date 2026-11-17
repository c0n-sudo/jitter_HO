import time
import random
import pyautogui

INTERVAL = 50 # in sec movement
JITTER = 10 # random movements in sec
BAR_WIDTH = 30 # bar size as symbole

def render_bar(elapsed, total, count):
    ratio = min(elapsed / total, 1)
    filled = int(BAR_WIDTH * ratio)
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)
    remaining = max(int(total - elapsed), 0)
    print(
        f"\r[{bar}] next move in {remaining:2d}s | move: {count}",
        end="",
        flush=True,
    )



print("Jitter running... kill task strg+c.")

count = 0
try:
    while True:
        wait = INTERVAL + random.randnit(-JITTER, JITTER)
        start = time.time()
        while (elapsed := time.time() - start) < wait:
               render_bar(elapsed, wait, count)
               time.sleep(0.5)


        pyautogui.moveRel(1, 0)
        pyautogui.moveRel(-1, 0)
        count += 1
except KeyboardInterrupt:
    print("\n\nPaused.")