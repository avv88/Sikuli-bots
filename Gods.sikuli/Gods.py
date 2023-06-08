Settings.MinSimilarity=0.85
import gc
MODE = 2
Debug.on(3)
imgBuy2500 = "imgBuy.png"
imgDiv = "imbDiv.png"
imgConfirm = Pattern("imgConfirm.png").targetOffset(-139,2)
imgScroll = Pattern("imgScroll.png").targetOffset(-10,-1)
wait(5)
imgBuy = imgBuy2500
if (MODE == 1):
    click(imgScroll)
    click()
    for x in range(1):
        if exists(imgBuy):
            click(imgBuy)
            wait(1)
            if exists(imgConfirm):
                click(imgConfirm)
    click(imgScroll)
    for x in range(1000000):
        if exists(imgBuy):
            click(imgBuy)
            wait(1)
            if exists(imgConfirm):
                click(imgConfirm)
if (MODE == 2):
    while True:
        if exists(imgDiv):
            click(imgDiv)
            wait(1)
            if exists(imgConfirm):
                click(imgConfirm)