import java.awt.Toolkit
cant = Pattern("cant.png").similar(0.82)
wait(5)
idle = 0
def MouseHold(img, duration = .5):
    hover(img)
    mouseDown(Button.LEFT)
    wait(duration)
    mouseUp(Button.LEFT)
while True:
    if not exists(Pattern("1600933850283.png").similar(0.84)):
        java.awt.Toolkit.getDefaultToolkit().beep()
    if not exists("1600927991934.png") or exists(Pattern("1600928444835.png").similar(0.79)):
        wait(60)
        idle += 1
        if idle >= 30:
            type(Key.SPACE)
            idle = 0
        continue
    wait(60*29)
    while exists(cant):
        click("1600928148231.png")
        wait(60)
        click(Pattern("1600928621802.png").targetOffset(-7,-42))
        if exists(cant):
            break
    if exists("1600928322302.png"):
        MouseHold(Pattern("1600928345404.png").similar(0.95).targetOffset(-103,-2))