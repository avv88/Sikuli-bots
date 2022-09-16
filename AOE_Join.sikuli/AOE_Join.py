import gc
imgMultiplayer = Pattern("imgMultiplayer.png").similar(0.90)
imgShowList = Pattern("1531201337012.png").similar(0.90)
imgJoin = Pattern("imgJoin.png").similar(0.91)
imgNotFound = Pattern("imgNotFound.png").similar(0.90)
imgRefresh = Pattern("imgRefresh.png").similar(0.90)
ImgFound = Pattern("1531203588538.png").similar(0.91)
imgReady = Pattern("imgReady.png").exact().targetOffset(-46,-4)
imgOver = Pattern("imgOver.png").similar(0.91)
img15 = "img15.png"
imgCancelled = Pattern("imgCancelled.png").similar(0.92).targetOffset(4,27)
while True:
    if exists(imgMultiplayer):
        click(imgMultiplayer)
        wait(1)
    if exists(imgShowList):
        click(imgShowList)
        wait(1)
    if exists(ImgFound):
        click(imgJoin)
        wait(5)
    if exists(imgNotFound):
        click(imgRefresh)
    if exists(imgReady):
        click(imgReady)
    if exists(imgOver):
        type(Key.F10)
        wait(1)
        type(Key.ENTER)
        wait(1)
        type(Key.ENTER)
        wait(1)        
        type(Key.ENTER)
        wait(1)
    if exists(img15):
        wait(15)
        if exists(img15):
            type(Key.ESC)
            wait(1)
            type(Key.ESC)
    if exists(imgCancelled):
        click(imgCancelled)
    gc.collect()