#setThrowException(False)
import java.awt.Toolkit
import gc
#Debug.setUserLogFile("c://Sikuli_Log_User.txt")
#Debug.user("text, %1",23)
Debug.on(3)
Debug.setLogFile("C://Sikuli_Log.txt")
faultCounter = 0
imgPlay = Pattern("1515451952989.png").similar(0.96)
imgPlayOffs = Pattern("1515451952989.png").similar(0.96).targetOffset(57,-1)
imgCustom = Pattern("1515452091080.png").similar(0.96)
imgCustomOffs = Pattern("1515452091080.png").similar(0.96).targetOffset(46,0)
imgModeSelector = Pattern("imgModeSelector.png").similar(0.80).targetOffset(-49,-37)
imgModeSelectorOffs = Pattern("imgModeSelector.png").similar(0.80).targetOffset(16,-33)
imgModeOpn = Pattern("imgModeOpn.png").similar(0.80).targetOffset(-64,-12)
imgModeOpnOffs = Pattern("imgModeOpn.png").similar(0.80).targetOffset(1,-11)
imgDmIcon = "1515452334096.png"
imgModeOK = "1515452349051.png"
imgModeOKOffs = Pattern("1515452349051.png").targetOffset(27,-2)
imgStart = "1515452390720.png"
imgStartOffs = Pattern("1515452390720.png").targetOffset(63,-3)
imgOKError = "1515495530809.png"
imgOKErrorOffs = Pattern("1515495530809.png").targetOffset(44,-4)
imgTeamView = Pattern("imgTeamView.png").targetOffset(171,60)
imgTeamView2 = Pattern("imgTeamView2.png").targetOffset(186,44)
imgLogin = Pattern("1515509104373.png").targetOffset(-97,1)
imgLoginOffs = Pattern("1515509104373.png").targetOffset(30,10)
imgPassword = Pattern("1515509226400.png").targetOffset(-76,7)
imgPasswordOffs = Pattern("1515509226400.png").targetOffset(-7,9)

imgLoginBtn = "1515509033316.png"
imgLoginBtnOffs = Pattern("1515509033316.png").targetOffset(57,-6)
imgClose = "1515592164379.png"
imgCloseOffs = Pattern("1515592164379.png").targetOffset(33,-1)
imgCloseNew = "imgCloseNew.png"
imgCloseNewOffs = Pattern("imgCloseNew.png").targetOffset(33,-1)
imgCloseAd = "imgCloseAd.png"
imgCloseAdOffs = Pattern("imgCloseAd.png").targetOffset(34,-1)
imgTryAgain = "imgTryAgain.png"
imgTryAgainOffs = Pattern("imgTryAgain.png").targetOffset(29,0)
imgDaily = "imgDaily.png"
imgDailyOffs = Pattern("imgDaily.png").targetOffset(33,-2)
imgHp = Pattern("imgHp.png").similar(0.73)
imgPlayBL =Pattern("imgPlayBL.png").similar(0.90)
imgQcTask = Pattern("imgQcTask.png").similar(0.97)
imgServer = Pattern("imgServer.png").targetOffset(176,0)
imgServerOffs =  Pattern("imgServer.png").targetOffset(176,0)
imgConnectBtn = Pattern("imgConnectBtn.png").similar(0.95)
imgConnectBtnOffs = Pattern("imgConnectBtn.png").similar(0.95).targetOffset(48,-3)
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
while True:
    if exists(imgTeamView):
        App.focus("Taskmgr")
        click(imgTeamView)
    if exists(imgTeamView2):
        App.focus("Taskmgr")
        click(imgTeamView2)
    faultCounter += 1
    if exists(imgPlay):
        PersistentClick(imgPlay, imgPlayOffs)
        wait(2)
    if exists (imgCustom):
        PersistentClick(imgCustom, imgCustomOffs)
    if exists (imgModeSelector):
        PersistentClick(imgModeSelector, imgModeSelectorOffs)
    if exists (imgModeOpn):
        PersistentClick(imgModeOpn, imgModeOpnOffs)
    if exists(imgDmIcon):
        PersistentClick(imgModeOK, imgModeOKOffs) 
        wait(2)
    if exists(imgStart):
        PersistentClick(imgStart, imgStartOffs)
        if not exists(imgStart):
            faultCounter = 0
            #wait(300)
    while exists(imgHp):
        keyDown("f")
        wait(3)
        keyUp()
    if exists(imgOKError): #разные ошибки
        PersistentClick(imgOKError, imgOKErrorOffs)       
    if exists(imgLoginBtn): #выкинуло из аккаунта
        PersistentClick(imgLogin, imgLoginOffs)
        type("!!!")
        PersistentClick(imgPassword, imgPasswordOffs)
        type("!!!")
        PersistentClick(imgLoginBtn, imgLoginBtnOffs)
        wait(60)
    if exists(imgClose): #разные сообщения и ошибки
        PersistentClick(imgClose, imgCloseOffs)
    if exists(imgTryAgain): #дисконнект
        PersistentClick(imgTryAgain, imgTryAgainOffs)
    if exists(imgCloseAd):
        PersistentClick(imgCloseAd, imgCloseAdOffs)
    if exists(imgDaily):
        PersistentClick(imgDaily, imgDailyOffs)
        wait(10)
    if exists(imgCloseNew): 
        PersistentClick(imgCloseNew, imgCloseNewOffs)
        wait(3)
    if exists(imgServer):
        while not exists (imgConnectBtn):
            click(imgServer)
        PersistentClick(imgConnectBtn, imgConnectBtnOffs)
    if faultCounter > 50:
        App.focus("Taskmgr")
        if exists(imgQcTask):
            click(imgQcTask)
            wait(2)
            type(Key.DELETE)
            wait(30)
        App.focus("BethesdaNetLauncher")
        wait(5)
        if exists(imgPlayBL):
            click(imgPlayBL)
            wait(5)
            if exists(imgPlayBL):
                click(imgPlayBL)
            wait(250)
            App.focus("Диспетчер")
            App.focus("Quake Champions")
    if faultCounter > 100:    
        while True:
            wait(5)
            java.awt.Toolkit.getDefaultToolkit().beep()
    gc.collect()