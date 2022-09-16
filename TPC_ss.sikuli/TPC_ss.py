Debug.on(3)
import time
import shutil
import os
tut = "1569339755302.png"
msg = "1569339812837.png"
mmenu = Pattern("mmenu.png").targetOffset(-4,92)
menubtn = Pattern("menubtn.png").targetOffset(0,-19)
confirm = Pattern("confirm.png").targetOffset(102,27)
wait(5)
screenshots = 1000

while True:
    if exists(tut):
        click(tut)
        wait(6)
        screenshots = screenshots + 1
        App.focus('The Protectors')
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        if os.path.isfile(regionImage):
            shutil.move(regionImage, os.path.join(r'C:\Screenshots', str(screenshots)+'.png'))
        wait(9)
    if exists(msg):
        click(msg)
        wait(1)
    if exists(menubtn):
        click(menubtn)
        wait(1)
    if exists(mmenu):
        click(mmenu)
        wait(1)
    if exists(confirm):
        click(confirm)
        wait(10)
    