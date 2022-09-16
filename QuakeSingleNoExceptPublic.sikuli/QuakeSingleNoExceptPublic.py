#setThrowException(False)
import java.awt.Toolkit
import gc
#Debug.setUserLogFile("c://Sikuli_Log_User.txt")
#Debug.user("text, %1",23)
Debug.on(3)
Debug.setLogFile("C://Sikuli_Log.txt")
faultCounter = 0
imgQC = "imgQC.png"
imgPlay = Pattern("1515451952989.png").similar(0.96)
imgPlayOffs = Pattern("1515451952989.png").similar(0.96).targetOffset(57,-1)
imgStart = Pattern("1515452390720.png").similar(0.91)
imgStartOffs = Pattern("1515452390720.png").targetOffset(63,-3)
imgOKError = Pattern("imgOKError.png").similar(0.87)
imgOKErrorOffs = Pattern("imgOKError.png").similar(0.87).targetOffset(31,-4)
imgLogin = Pattern("1515509104373.png").similar(0.90).targetOffset(-97,1)
imgLoginOffs = Pattern("1515509104373.png").targetOffset(30,10)
imgPassword = Pattern("1515509226400.png").similar(0.85).targetOffset(-76,7)
imgPasswordOffs = Pattern("1515509226400.png").targetOffset(-7,9)

imgLoginBtn = Pattern("1515509033316.png").similar(0.87)
imgLoginBtnOffs = Pattern("1515509033316.png").targetOffset(57,-6)
imgClose = Pattern("imgClose.png").similar(0.85)
imgCloseOffs = Pattern("imgClose.png").similar(0.85).targetOffset(48,-1)
imgCloseNew = Pattern("imgCloseNew.png").similar(0.88)
imgCloseNewOffs = Pattern("imgCloseNew.png").targetOffset(33,-1)
imgCloseAd = Pattern("imgCloseAd.png").similar(0.87)
imgCloseAdOffs = Pattern("imgCloseAd.png").targetOffset(34,-1)
imgTryAgain = Pattern("imgTryAgain.png").similar(0.85)
imgTryAgainOffs = Pattern("imgTryAgain.png").targetOffset(29,0)
imgDaily = Pattern("imgDaily.png").similar(0.85)
imgDailyOffs = Pattern("imgDaily.png").targetOffset(33,-2)
imgHp = Pattern("imgHp.png").similar(0.73)
imgPlayBL =Pattern("imgPlayBL.png").similar(0.94)
imgRunningBL = Pattern("imgRunningBL.png").similar(0.97)
imgQcTask = Pattern("imgQcTask.png").similar(0.97)
imgServer = Pattern("imgServer.png").similar(0.83).targetOffset(176,0)
imgServerOffs =  Pattern("imgServer.png").targetOffset(176,0)
imgConnectBtn = Pattern("imgConnectBtn.png").similar(0.95)
imgConnectBtnOffs = Pattern("imgConnectBtn.png").similar(0.95).targetOffset(48,-3)
imgCustom = Pattern("imgCustom.png").similar(0.87)
imgCustomOffs = Pattern("imgCustom.png").similar(0.87).targetOffset(54,23)
imgGameType = Pattern("imgGametype.png").similar(0.86).targetOffset(-51,6)
imgGameTypeOffs = Pattern("imgGametype.png").similar(0.86).targetOffset(28,5)
imgGameList = Pattern("imgGameList.png").similar(0.86).targetOffset(-48,-54)
imgGameListOffs = Pattern("imgGameList.png").similar(0.86).targetOffset(-24,-52)
imgDM = Pattern("imgDM.png").similar(0.88)
imgOk = Pattern("imgOK.png").similar(0.89)
imgOkOffs = Pattern("imgOK.png").similar(0.89).targetOffset(35,-3)
imgArcade = Pattern("imgArcade.png").similar(0.91)
#Pattern("imgArcade.png").similar(0.89).targetOffset(8,-75)
imgSearch = Pattern("imgSearch.png").similar(0.88)
imgSearchOffs = Pattern("imgSearch.png").targetOffset(49,-3)
imgBlOk = Pattern("imgBlOk.png").similar(0.90)
imgCrash = Pattern("imgCrash.png").similar(0.90).targetOffset(50,-2)
def PersistentClick(img, imgOffs):
    try:
        click(img)
        wait(1)
        if exists(img):
            click(img)
            wait(1)
        else:
            return
        if exists(img):
            click(imgOffs)
            wait(1)
        else:
            return
        if exists(img):
            hover(imgOffs)
            wait(1)
            mouseDown(Button.LEFT)
            wait(1)
            mouseUp()
            wait(1)
    except:
        return
def PressButtons():
    if exists(imgStart):
        PersistentClick(imgStart, imgStartOffs)
        if not exists(imgStart):
            faultCounter = 0
    while exists(imgHp):
        keyDown("f")
        wait(3)
        keyUp()
while True:
    faultCounter += 1
    #start
    if exists(imgCloseNew): 
        PersistentClick(imgCloseNew, imgCloseNewOffs)
    if exists(imgPlay):
        PersistentClick(imgPlay, imgPlayOffs)
        wait(2)
    PressButtons()
    if exists(imgRunningBL):
        App.focus("Taskmgr")
        App.focus("Диспетчер")
        App.focus("BethesdaNetLauncher")
        wait(2)
    PressButtons()
    if exists(imgPlayBL):
        click(imgPlayBL)
        wait(5)
    PressButtons()
    #if exists(imgCustom):
    #    PersistentClick(imgCustom, imgCustomOffs)
    #    wait(2)
    #    hover(imgQC)
    if exists(imgArcade):
        hover(imgArcade)
    if exists(imgSearch):
        PersistentClick(imgSearch, imgSearchOffs)
    PressButtons()
    if exists(imgGameType):
        PersistentClick(imgGameType, imgGameTypeOffs)
        if not exists(imgGameList):
            click(imgGameType)
        wait(2)
    PressButtons()
    if exists(imgGameList):
        PersistentClick(imgGameList, imgGameListOffs)
        wait(2)
    PressButtons()
    if exists(imgDM):
        PersistentClick(imgOk, imgOkOffs)
        wait(2)
    PressButtons()
    #loop
    PressButtons()
            #wait(300)
    if exists(imgOKError): #разные ошибки
        PersistentClick(imgOKError, imgOKErrorOffs)       
    if exists(imgLoginBtn): #выкинуло из аккаунта
        PersistentClick(imgLogin, imgLoginOffs)
        type("!!!")
        PersistentClick(imgPassword, imgPasswordOffs)
        type("!!!")
        PersistentClick(imgLoginBtn, imgLoginBtnOffs)
        wait(60)
    if exists(imgCrash):
        click(imgCrash)
    PressButtons()
    if exists(imgClose): #разные сообщения и ошибки
        PersistentClick(imgClose, imgCloseOffs)
    if exists(imgTryAgain): #дисконнект
        PersistentClick(imgTryAgain, imgTryAgainOffs)
    PressButtons()
    if exists(imgCloseAd):
        PersistentClick(imgCloseAd, imgCloseAdOffs)
    if exists(imgDaily):
        PersistentClick(imgDaily, imgDailyOffs)
        wait(10)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
    PressButtons()
    if exists(imgServer):
        while not exists (imgConnectBtn):
            click(imgServer)
        PersistentClick(imgConnectBtn, imgConnectBtnOffs)
    PressButtons()
    if exists(imgBlOk):
        click(imgBlOk)
    if exists(imgRunningBL):
        try:
            hover(imgRunningBL)
            click(imgRunningBL)
            App.focus("Taskmgr")
            App.focus("Диспетчер")
            App.focus("BethesdaNetLauncher")
            hover(imgRunningBL)
            click(imgRunningBL)
            click
            wait(2)
        except:
            pass
        wait(10)
        if not exists(imgRunningBL) and not exists(imgPlayBL):
            wait(900)
    if exists(imgPlayBL):
            click(imgPlayBL)
            wait(900)
            if exists(imgPlayBL):
                click(imgPlayBL)
            wait(900)
            App.focus("Диспетчер")
            App.focus("Quake Champions")
    if False: #faultCounter > 1000:
        screen = Screen()
        file = screen.capture(screen.getBounds())
        #print("Saved screen as "+file)
        App.focus("Taskmgr")
        if exists(imgQcTask):
            click(imgQcTask)
            wait(2)
            type(Key.DELETE)
            wait(30)
        App.focus("BethesdaNetLauncher")
        wait(5)
        if exists(imgRunningBL):
            App.focus("Taskmgr")
            App.focus("Диспетчер")
            App.focus("BethesdaNetLauncher")
            if not exists(imgRunningBL):
                continue
            try:
                hover(imgRunningBL)
                mouseDown(Button.LEFT)
                wait(1)
                mouseUp()
                wait(900)
                #hover(imgRunningBL)
                #click(imgRunningBL)
                #click
                #wait(2)
            except:
                pass
        if exists(imgPlayBL):
            click(imgPlayBL)
            wait(900)
            if exists(imgPlayBL):
                click(imgPlayBL)
            wait(900)
            App.focus("Диспетчер")
            App.focus("Quake Champions")
    if False: #faultCounter > 10000000:    
        while True:
            wait(5)
            java.awt.Toolkit.getDefaultToolkit().beep()
    gc.collect()