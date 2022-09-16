#1280x800 window
import gc
import time
from datetime import datetime
Settings.MinSimilarity=0.85

loginImg = Pattern("loginImg.png").targetOffset(-15,111)
loginDoneImg = "loginDoneImg.png"
hoverOn = "hoverOn.png"
storeBtn = Pattern("storeBtn.png").targetOffset(19,-48)
storeBtn2 = Pattern("storeBtn2.png").targetOffset(57,-63)
storeBtn3 = "storeBtn3.png"
settingsBtn = "settingsBtn.png"
exitBtn = Pattern("exitBtn.png").targetOffset(31,-61)
logoffBtn = "logoffBtn.png"
def CheckConnection():
    if exists(loginImg):
        Login()
def Login():
    if exists(loginImg):
        paste(loginImg, "!!!")
        type(Key.ENTER)
    else:
        return
    while not exists(loginDoneImg):
        wait(5)
    type(Key.ESC)
    wait(1)
time_online = time.time()
def Logoff():
    if exists(settingsBtn):
        click(settingsBtn)
        wait(4)
    if exists(exitBtn):
        click(exitBtn)
        wait(4)
    if exists(logoffBtn):
        click(logoffBtn)
        wait(20)
wait(5)
while True:
    CheckConnection()
    hover(hoverOn)
    if exists(storeBtn):
        click(storeBtn)
        wait(5)
        if exists(hoverOn):
            hover(hoverOn)
    if exists(storeBtn2):
        click(storeBtn2)
        wait(5)
        if exists(hoverOn):
            hover(hoverOn)
    if exists(storeBtn3):
        click(storeBtn3)
        wait(5)
        if exists(hoverOn):
            hover(hoverOn)
    if (time.time() - time_online) > 72000: #20*60*60 sec
        Logoff()
        wait(7200)
        time_online = time.time()