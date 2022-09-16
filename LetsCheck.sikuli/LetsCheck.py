timerOk1 = Pattern("timerOk.png").exact()
timerOk2 = Pattern("timerOk2.png").exact()
contr = Pattern("contr.png").similar(0.76)
hoveron = Pattern("hoveron.png").similar(0.91)
while 1:
    wait(500)
    if not exists(timerOk1) or not exists(timerOk2):
        hover(contr)
        mouseDown(Button.LEFT)
        mouseUp()
        wait(3)
        mouseDown(Button.LEFT)
        mouseUp
        hover(hoveron)

        