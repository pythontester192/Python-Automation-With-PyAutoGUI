import pyautogui as pg
import keyboard as key
import time
import random

time.sleep(3)
# print(pg.position())

#position of search box: x=643, y=103
pg.leftClick(643, 103)      
time.sleep(1)
key.write("#python")    
time.sleep(2)

#position of hashtag: x= 650, y= 164
pg.leftClick(650, 164)
time.sleep(3)

#position of image post: x=314, y=529
pg.leftClick(314, 529)
time.sleep(3)

list = ["That's Awesome", "Great One", "Perfect"]

for i in range(5):
    #position of like button: x=729, y=566
    pg.doubleClick(418, 388)
    time.sleep(1)

    #position of comment button: x=888, y=680
    pg.leftClick(888, 680, 1)
    msg = random.choice(list)
    pg.typewrite(msg)
    time.sleep(1)
    pg.press("enter")
    time.sleep(5)

    #position of next button: x=1322, y=391
    pg.leftClick(1322, 391)
    time.sleep(3)

