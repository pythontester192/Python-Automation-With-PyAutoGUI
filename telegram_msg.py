import pyautogui as pg
import time

time.sleep(3)
print(pg.position())

pg.leftClick(660, 748, 1, 1)
time.sleep(1)
pg.typewrite("web.telegram.org/z/")
time.sleep(1)
pg.press("enter")
time.sleep(1)
pg.leftClick(182, 174, 1, 1)
time.sleep(1)

for i in range(10):
    pg.typewrite("SPAM MSG BOT USING PYAUTOGUI")
    pg.press("enter")
    time.sleep(1)

print("DONE!")