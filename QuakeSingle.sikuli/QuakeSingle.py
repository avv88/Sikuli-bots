#setThrowException(False)
import java.awt.Toolkit
import gc
faultCounter = 0
imgPlay = Pattern("1515451952989.png").similar(0.96)
imgPlayOffs = Pattern("1515451952989.png").similar(0.96).targetOffset(57,-1)
imgCustom = Pattern("1515452091080.png").similar(0.96)
imgCustomOffs = Pattern("1515452091080.png").similar(0.96).targetOffset(46,0)
imgModeSelector = Pattern("1515453054069.png").similar(0.80).targetOffset(-35,-35)
imgModeSelectorOffs = Pattern("1515453054069.png").similar(0.80).targetOffset(30,-37)
imgModeOpn = Pattern("1515452286237.png").targetOffset(-49,51)
imgModeOpnOffs = Pattern("1515452286237.png").targetOffset(2,51)
imgDmIcon = "1515452334096.png"
imgModeOK = "1515452349051.png"
imgModeOKOffs = Pattern("1515452349051.png").targetOffset(27,-2)
imgStart = "1515452390720.png"
imgStartOffs = Pattern("1515452390720.png").targetOffset(63,-3)
imgOKError = "1515495530809.png"
imgOKErrorOffs = Pattern("1515495530809.png").targetOffset(44,-4)
imgTeamView = Pattern("1515455367862.png").targetOffset(215,76)
imgLogin = Pattern("1515509104373.png").targetOffset(-97,1)
imgLoginOffs = Pattern("1515509104373.png").targetOffset(30,10)
imgPassword = Pattern("1515509226400.png").targetOffset(-76,7)
imgPasswordOffs = Pattern("1515509226400.png").targetOffset(-7,9)

imgLoginBtn = "1515509033316.png"
imgLoginBtnOffs = Pattern("1515509033316.png").targetOffset(57,-6)
imgClose = "1515592164379.png"
imgCloseOffs = Pattern("1515592164379.png").targetOffset(33,-1)
imgPlayBL ="1515542207936.png"



while True:
    gc.collect()
    faultCounter += 1
    if exists(imgPlay):
        #App.focus("WordPad")
        click(ImgPlay)
        wait(1)
        click(imgPlayOffs)
        hover(imgPlay)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(2)
    if exists (imgCustom):
        click(imgCustom)
        wait(1)
        click(imgCustomOffs)
        hover(imgCustom)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
        if exists (imgModeSelector):
            click(imgModeSelector)
            wait(1)
            click(imgModeSelectorOffs)
            wait(1)
            if exists(imgModeSelector):
                hover(imgModeSelector)
                wait(1)
                mouseDown(Button.LEFT)
                wait(1)
                mouseUp()
                wait(1)
    if exists (imgModeOpn):
        click(imgModeOpn)
        wait(1)
        click(imgModeOpnOffs)
        hover(imgModeOpn)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
    if exists(imgDmIcon):
        click(imgModeOk)
        wait(1)
        click(imgModeOkOffs)
        hover(imgModeOk)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
        
    if exists(imgStart):
        #popup(str(faultCounter))
        faultCounter = 0
        #App.focus("WordPad")
        click(imgStart)
        wait(2)
        click(imgStartOffs)
        hover(imgStart)
        wait(2)
        mouseDown(Button.LEFT)
        wait(2)
        mouseUp()
    if exists(imgOKError): #разные ошибки
        click(imgOKError)
        wait(2)
        click(imgOKErrorOffs)
        hover(imgOKError)
        wait(2)
        mouseDown(Button.LEFT)
        wait(2)
        mouseUp()
        
    if exists(imgTeamView):
        App.focus("GPU-Z")
        click(imgTeamView)
    if exists(imgLoginBtn): #выкинуло из аккаунта
        click(imgLogin)
        wait(1)
        click(imgLoginOffs)
        hover(imgLogin)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
        type("JcJet")
        click(imgPassword)
        wait(1)
        click(imgPasswordOffs)
        hover(imgPassword)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(1)
        type("!!!")
        click(imgLoginButton)
        wait(1)
        click(imgLoginButtonOffs)
        hover(imgLoginButton)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
        wait(60)
    if exists(imgClose): #разные сообщения и ошибки
        click(imgClose)
        wait(1)
        click(imgCloseOffs)
        hover(imgClose)
        wait(1)
        mouseDown(Button.LEFT)
        wait(1)
        mouseUp()
    if faultCounter == 35:
        App.close("Quake Champions")
        wait(30)
        App.focus("BethesdaNetLauncher")
        wait(5)
        click(imgPlayBL)
        wait(250)
        App.focus("Quake Champions")
    if faultCounter > 50:    
        while True:
            wait(5)
            java.awt.Toolkit.getDefaultToolkit().beep()
    gc.collect()
        